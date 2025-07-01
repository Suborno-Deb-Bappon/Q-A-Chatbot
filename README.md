# Q-A-Chatbot

## Project Overview

This project is a Question-Answering Chatbot built using Python, leveraging several libraries for natural language processing, vector databases, and web application development. It allows users to ask questions and receive answers based on information stored in a ChromaDB vector database. The application is built using FastAPI and Streamlit, providing both an API endpoint and a user-friendly interface for interacting with the chatbot.

## Installation

To set up the project, follow these steps:

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

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

The project includes both a FastAPI backend and a Streamlit frontend.

#### FastAPI Backend

1.  **Run the FastAPI application:**

    ```bash
    uvicorn app:app --reload
    ```

    This will start the FastAPI server, typically on `http://127.0.0.1:8000`.

#### Streamlit Frontend

1.  **Run the Streamlit application:**

    ```bash
    streamlit run main.py
    ```

    This will open the Streamlit application in your web browser, allowing you to interact with the chatbot through a user interface.

### Interacting with the API

You can interact with the chatbot via the FastAPI endpoint. Example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "Your question here"}' http://127.0.0.1:8000/query
```

Replace `"Your question here"` with your actual question.

### Environment Variables

Consider using a `.env` file to manage environment variables, especially for API keys or database credentials.

```python
# Example .env file
OPENAI_API_KEY=your_openai_api_key
```

Load the environment variables in your `app.py` or `query.py` files using `python-dotenv`.

## Features

*   **Question Answering:** Answers user questions based on the data stored in the ChromaDB vector database.
*   **ChromaDB Integration:** Uses ChromaDB for efficient storage and retrieval of embeddings.
*   **FastAPI Backend:** Provides an API endpoint for querying the chatbot.
*   **Streamlit Frontend:** Offers a user-friendly interface for interacting with the chatbot.
*   **Langchain Integration:** Leverages Langchain for building the chatbot logic.
*   **OpenAI Integration:** (Potentially) Uses OpenAI models for embeddings and text generation. Check the code for actual API key usage.
*   **.devcontainer Configuration:** Includes a `.devcontainer` directory for development in a containerized environment, ensuring consistent development setup.

## Project Structure

*   `app.py`: FastAPI application that handles API requests.
*   `main.py`: Streamlit application for the user interface.
*   `query.py`: Contains the logic for querying the ChromaDB and generating answers.
*   `chroma_db/`: Directory containing the ChromaDB database files.
*   `docs/`: (If exists) Documentation for the project.
*   `requirements.txt`: List of Python dependencies.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `.devcontainer/`: Configuration files for developing inside a Docker container.

## Dependencies

The project relies on the following Python packages:

*   `fastapi`: For building the API.
*   `streamlit`: For creating the user interface.
*   `langchain`: For building the chatbot logic.
*   `chromadb`: For the vector database.
*   `openai`: For interacting with OpenAI models (if used).
*   `uvicorn`: ASGI server for running the FastAPI application.
*   `python-dotenv`: For loading environment variables.
*   `tiktoken`: For tokenizing text.
*   Other dependencies listed in `requirements.txt`.
