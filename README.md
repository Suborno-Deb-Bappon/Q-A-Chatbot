# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python, leveraging libraries such as Langchain, ChromaDB, and OpenAI. The chatbot ingests documents, stores them in a vector database, and answers questions based on their content. It uses text splitting, embeddings, and a language model for relevant and informative answers. The application provides both a command-line interface (CLI) and a Streamlit-based web interface.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Suborno-Deb-Bappon/Q-A-Chatbot.git
    cd Q-A-Chatbot
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your OpenAI API key:**

    You need an OpenAI API key to use the language model. Set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Linux/macOS
    set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Windows
    ```

    Alternatively, set the API key in a `.env` file:

    ```
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Install `python-dotenv` if you use a `.env` file.

## Usage

The project includes these Python scripts:

*   `main.py`: Core logic for creating and querying the ChromaDB vector store.
*   `query.py`: Functions for querying the ChromaDB vector store and interacting with the language model.
*   `app.py`: Streamlit web interface for the chatbot.

### 1. Ingesting and Querying Documents (CLI)

1.  **Prepare your documents:**
    Place documents for the chatbot to learn from in the `docs` directory. Various document types are supported.

2.  **Run `main.py` to create the ChromaDB:**

    ```bash
    python main.py
    ```

    This script will:

    *   Load documents from the `docs` directory.
    *   Split documents into smaller chunks.
    *   Generate embeddings for each chunk using OpenAI.
    *   Store embeddings in a ChromaDB vector store in the `chroma_db` directory.

3.  **Run `query.py` to interact with the chatbot from the command line:**

    ```bash
    python query.py
    ```

    This script will:

    *   Load the ChromaDB vector store from the `chroma_db` directory.
    *   Prompt you to enter a question.
    *   Retrieve relevant documents from the vector store based on your question.
    *   Use the language model to generate an answer.
    *   Print the answer to the console.

### 2. Using the Streamlit Web Interface

1.  **Ensure the ChromaDB is created:**
    Run `python main.py` to create the vector store before starting the Streamlit app.

2.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    This command will:

    *   Start a Streamlit server.
    *   Open the chatbot interface in your web browser.

3.  **Interact with the chatbot:**

    *   Type your question in the input box.
    *   Press Enter or click the "Send" button.
    *   The chatbot will display the answer in the chat window.

## Features

*   **Document Ingestion:** Loads and processes documents from the `docs` directory, supporting various formats.
*   **Text Splitting:** Splits large documents into smaller chunks for better question answering.
*   **Embeddings:** Generates vector embeddings of document chunks using OpenAI's API.
*   **Vector Database:** Stores document embeddings in ChromaDB for efficient similarity search.
*   **Question Answering:** Uses Langchain and OpenAI to answer questions based on the ingested documents.
*   **Command-Line Interface:** Provides a CLI for interacting with the chatbot.
*   **Streamlit Web Interface:** Offers a user-friendly web interface.
*   **Environment Variable Configuration:** Uses environment variables (or a `.env` file) for sensitive information like the OpenAI API key.

## Directory Structure

```
Q-A-Chatbot/
├── .devcontainer/       # Development container configuration (optional)
├── .gitignore          # Specifies intentionally untracked files that Git should ignore
├── __pycache__/        # Python bytecode cache directory
├── app.py              # Streamlit web application for the chatbot
├── chroma_db/          # Directory where ChromaDB stores the vector database
├── docs/               # Directory to place the documents you want the chatbot to learn from
├── main.py             # Script for creating the ChromaDB vector store from documents
├── query.py            # Script for querying the ChromaDB vector store from the command line
├── requirements.txt    # List of Python dependencies
└── README.md           # This file
```

## Dependencies

The project uses the following dependencies:

*   `langchain`: For building language model applications.
*   `chromadb`: For storing and querying vector embeddings.
*   `openai`: For accessing OpenAI's language models and embeddings.
*   `streamlit`: For creating the web interface.
*   `python-dotenv`: For loading environment variables from a `.env` file.
*   `tiktoken`: For tokenizing text for OpenAI models.

A full list of dependencies is available in `requirements.txt`.