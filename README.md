# Q-A-Chatbot

## Overview

This project implements a Question-Answering Chatbot using Python. It leverages several libraries for natural language processing, vector storage, and web application development, including Langchain, ChromaDB, and Streamlit. The chatbot is designed to provide answers to questions based on a given knowledge base (presumably stored in the `docs` directory and handled by ChromaDB).

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

    This will install all the necessary packages listed in the `requirements.txt` file, including `langchain`, `chromadb`, `streamlit`, and other dependencies.

4.  **Set up your OpenAI API key:**

    The project likely uses the OpenAI API. You will need to set your API key as an environment variable.

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Linux/macOS
    set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Windows
    ```

    Or, you can create a `.env` file in the project root directory and add the API key there:

    ```
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

## Usage

1.  **Prepare your documents:**

    Place the documents you want the chatbot to use as its knowledge base in the `docs` directory.  The code likely handles loading and processing these documents to create embeddings.

2.  **Run the main script:**

    This script might handle the initial setup of the ChromaDB vector store.

    ```bash
    python main.py
    ```

    Or, if there is specific data ingestion/processing within `query.py`, run that file:

    ```bash
     python query.py
    ```

3.  **Run the Streamlit application:**

    The `app.py` file likely contains the Streamlit application that provides the user interface for the chatbot.

    ```bash
    streamlit run app.py
    ```

    This will start the Streamlit app, and you can access it in your web browser, usually at `http://localhost:8501`.

4.  **Interact with the chatbot:**

    In the Streamlit app, you should be able to enter your questions, and the chatbot will provide answers based on the content of the documents in the `docs` directory.

## Features

*   **Question Answering:** Provides answers to user questions based on a pre-defined knowledge base.
*   **Integration with ChromaDB:** Utilizes ChromaDB for efficient storage and retrieval of document embeddings.
*   **Streamlit UI:** Offers a user-friendly interface for interacting with the chatbot.
*   **Uses Langchain:** Leverages Langchain for constructing chains of operations, such as document loading, text splitting, embedding generation, and question answering.
*   **OpenAI Integration:** Uses OpenAI\'s API for generating embeddings and possibly for generating answers.
*   **Document Loading:** Capable of loading and processing various document types (the specific types supported will depend on the implementation in `query.py` or `main.py`).
*   **Persistent Storage:** The ChromaDB vector store persists the embeddings, allowing for faster retrieval in subsequent sessions.

## Project Structure

*   `.devcontainer/`: Contains configuration for a development container environment.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__/`: Python\'s directory for storing compiled bytecode files.
*   `app.py`: The Streamlit application code, providing the user interface for the chatbot.
*   `chroma_db/`: Directory for storing ChromaDB data.
*   `docs/`: Directory for storing the documents used as the chatbot\'s knowledge base.
*   `main.py`: Likely contains the main script for setting up the ChromaDB vector store and processing documents.
*   `query.py`: Likely contains functions for querying the ChromaDB vector store and retrieving answers.
*   `requirements.txt`: A list of Python packages required to run the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

(Add license information here, e.g., MIT License, Apache 2.0, etc.)