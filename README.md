# Q-A-Chatbot

## Overview

This project implements a Question-Answering Chatbot using Python. It leverages libraries such as Langchain, ChromaDB, and OpenAI to create a chatbot capable of answering questions based on provided documents. The application is built using FastAPI and Streamlit, providing both an API endpoint and a user-friendly interface for interacting with the chatbot.

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
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the project root directory and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

### Running the API (FastAPI)

1.  Navigate to the project directory in your terminal.

2.  Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn app:app --reload
    ```

    This will start the API server, typically on `http://127.0.0.1:8000`.

### Running the Streamlit UI

1.  Ensure the API is running as described above.

2.  Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

    This will open the Streamlit UI in your web browser. By default, it usually opens at `http://localhost:8501`.

### Interacting with the Chatbot

*   **Streamlit UI:** Use the chat interface in the Streamlit application to ask questions. The chatbot will respond based on the documents it has been trained on (located in the `docs` directory).
*   **API Endpoint:** You can send POST requests to the appropriate API endpoint (check `app.py` for the exact route) to query the chatbot programmatically.

## Project Structure

```
Q-A-Chatbot/
├── .devcontainer/            # Configuration for development in a containerized environment
├── .gitignore               # Specifies intentionally untracked files that Git should ignore
├── __pycache__/             # Python's bytecode cache directory
├── app.py                   # FastAPI application code, defining API endpoints
├── chroma_db/               # ChromaDB database files
├── docs/                    # Documents used to train the chatbot
├── main.py                  # Streamlit application code for the chatbot UI
├── query.py                 # Code related to querying the ChromaDB and interacting with the language model
├── requirements.txt         # Lists the Python packages required to run the project
└── README.md                # This file
```

## Features

*   **Question Answering:** Answers questions based on the content of provided documents.
*   **API Endpoint:** Provides an API for programmatically querying the chatbot.
*   **Streamlit UI:** Offers a user-friendly chat interface.
*   **Uses Langchain:** Leverages Langchain for managing language model interactions.
*   **Uses ChromaDB:** Employs ChromaDB for vector storage and retrieval, enabling efficient similarity searches.
*   **OpenAI Integration:** Utilizes the OpenAI API for generating responses.

## Dependencies

The project relies on the following main libraries (see `requirements.txt` for a complete list):

*   `fastapi`: For creating the API.
*   `streamlit`: For building the user interface.
*   `langchain`: For language model integration.
*   `chromadb`: For vector database functionality.
*   `openai`: For accessing the OpenAI API.
*   `python-dotenv`: For managing environment variables.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

[Specify the license under which the project is released]
