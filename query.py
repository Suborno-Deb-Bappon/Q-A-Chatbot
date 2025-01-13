import os
import sys
import warnings
import streamlit as st

# Disable warnings
warnings.filterwarnings("ignore")

# Imports
import chromadb
from chromadb.config import Settings

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma


# Deployment-safe path configuration
def get_document_path():
    possible_paths = [
        "./docs/faq.txt",  # Local development
        "/mount/src/q-a-chatbot/docs/faq.txt",  # Streamlit Cloud
        os.path.join(os.path.dirname(__file__), "docs/faq.txt")  # Relative path
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    st.error("FAQ document not found in any of the expected locations")
    return None


@st.cache_resource
def get_llm():
    return ChatOpenAI(
        api_key=st.secrets["openai_api_key"],
        model="gpt-3.5-turbo",
        temperature=0.7
    )


@st.cache_resource
def get_embeddings():
    return OpenAIEmbeddings(
        model="text-embedding-3-small", 
        api_key=st.secrets["openai_api_key"]
    )


@st.cache_resource
def initialize_vectorstore():
    """Initialize the vector store using DuckDB + Parquet (bypassing SQLite)."""
    try:
        # 1) Get document path
        document_path = get_document_path()
        if not document_path:
            st.error("Could not find document path")
            return None

        # 2) Get embeddings
        embeddings = get_embeddings()

        # 3) Load and split documents
        documents = TextLoader(document_path).load()
        text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="\n")
        splits = text_splitter.split_documents(documents)

        # 4) Create a persist directory
        persist_directory = os.path.join(os.path.dirname(__file__), "duckdb_chroma_db")
        os.makedirs(persist_directory, exist_ok=True)

        # 5) Configure Chroma to use DuckDB + Parquet
        chroma_client = chromadb.Client(
            Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=persist_directory,
                anonymized_telemetry=False
            )
        )

        # 6) Create the vector store
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
            client=chroma_client,
            collection_name="faq_collection",
            persist_directory=persist_directory
        )
        
        return vectorstore
    except Exception as e:
        st.error(f"Error initializing vector store: {e}")
        return None


# Initialize vector store
vectorstore = initialize_vectorstore()


def setup_retriever(vectorstore):
    """Set up the retriever with the vector store"""
    if vectorstore is None:
        st.error("Vector store not initialized")
        return None
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )


# Get retriever
retriever = setup_retriever(vectorstore)


def format_docs(docs):
    """Format retrieved documents into a single string"""
    return "\n\n".join(doc.page_content for doc in docs)


# QA system prompt
qa_system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.

Context: {context}
Question: {input}
"""


# Create prompt template
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", qa_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# Chat history management
chat_history = []


def query(input_text):
    """
    Main query function that returns a response to the user input

    Args:
        input_text (str): User's input question

    Returns:
        dict: Generated response
    """
    # Check if vectorstore and retriever are initialized
    if vectorstore is None or retriever is None:
        return {"answer": "Error: Vector store not initialized. Cannot process query."}

    try:
        # Get LLM
        llm = get_llm()

        # Retrieve relevant documents
        retrieved_docs = retriever.invoke(input_text)
        context = format_docs(retrieved_docs)

        # Generate response using the context
        response = llm.invoke(
            qa_prompt.format_messages(
                chat_history=chat_history,
                input=input_text,
                context=context
            )
        ).content

        # Update chat history
        chat_history.extend([
            HumanMessage(content=input_text), 
            HumanMessage(content=response)
        ])

        return {"answer": response}

    except Exception as e:
        # Fallback for any unexpected errors
        print(f"Error processing query: {e}")
        return {"answer": f"I'm sorry, but I encountered an error: {str(e)}"}
