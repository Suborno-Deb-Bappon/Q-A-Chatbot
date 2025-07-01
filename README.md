# Q-A-Chatbot

## Overview

This project implements a Question-Answering Chatbot using Python. It leverages several libraries, including Langchain, ChromaDB, and OpenAI, to provide intelligent and context-aware responses to user queries. The chatbot is designed to ingest documents, create embeddings, and store them in a vector database (ChromaDB) for efficient retrieval. It then uses these embeddings and a language model (OpenAI) to generate answers to questions based on the ingested documents.

## Installation

To set up the Q-A-Chatbot, follow these steps:

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

    You will need an OpenAI API key to use the chatbot. You can obtain one from the [OpenAI website](https://platform.openai.com/).  Set the API key as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Linux/macOS
    set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Windows
    ```
    Or create a `.env` file in the root directory and add:
    ```
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```
    and ensure that your code reads from the `.env` file.

## Usage

1.  **Ingest Documents (Optional):**

    If you have documents you want the chatbot to answer questions about, place them in the `docs` directory. The `query.py` script handles document loading and embedding.

2.  **Run the `query.py` script:**

    This script handles the document ingestion, embedding, and querying logic.

    ```bash
    python query.py
    ```

    The `query.py` script likely contains functions to:

    *   Load documents from the `docs` directory.
    *   Split the documents into chunks.
    *   Create embeddings for the document chunks using OpenAI.
    *   Store the embeddings in ChromaDB.
    *   Define a question-answering chain using Langchain.
    *   Take a user query as input.
    *   Retrieve relevant document chunks from ChromaDB based on the query.
    *   Generate an answer using the language model.

3.  **Run the `app.py` for streamlit application:**

    ```bash
    streamlit run app.py
    ```

4.  **Run the `main.py` script:**

    This script uses FastAPI to set up endpoints, one for document processing and the other for query processing

    ```bash
    python main.py
    ```

## Features

*   **Document Ingestion:**  The chatbot can ingest documents from a specified directory (`docs`).
*   **Embedding Generation:** Uses OpenAI embeddings to create vector representations of the document content.
*   **Vector Storage:** Stores document embeddings in ChromaDB for fast and efficient retrieval.
*   **Question Answering:**  Leverages Langchain to create a question-answering chain that retrieves relevant documents and generates answers using a language model.
*   **API Endpoints:** Uses FastAPI to create API endpoint to handle document processing and query processing.
*   **Streamlit App:** Uses streamlit to create a chat interface

## File Structure

*   `.devcontainer/`: Contains configuration for a development container.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__/`: Contains compiled Python bytecode files.
*   `app.py`: Implements streamlit application.
*   `chroma_db/`: Directory to store chroma database.
*   `docs/`: Directory to store documents for the chatbot to learn from.
*   `main.py`: Implements FastAPI application for document processing and query processing.
*   `query.py`: Contains the core logic for document loading, embedding, and question answering.
*   `requirements.txt`: Lists the Python packages required to run the chatbot.

## Dependencies

The project relies on the following main Python libraries:

*   `langchain`: For creating question-answering chains.
*   `chromadb`: For storing and retrieving document embeddings.
*   `openai`: For generating embeddings and answering questions.
*   `fastapi`: For creating API endpoints.
*   `streamlit`: For developing interactive application
*   `python-dotenv`: For managing environment variables.

A complete list of dependencies can be found in `requirements.txt`.

## Contributing

Contributions to this project are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.