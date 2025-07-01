# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python. It leverages various libraries, including Langchain, ChromaDB, and FastAPI, to create a system where users can ask questions and receive answers based on a knowledge base.

## Installation

To set up the project, follow these steps:

1.  Clone the repository:

    ```bash
    git clone https://github.com/Suborno-Deb-Bappon/Q-A-Chatbot.git
    cd Q-A-Chatbot
    ```

2.  It is **highly recommended** to create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate # On Linux/macOS
    venv\Scripts\activate.bat # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Running the Chatbot Application:**

    The `app.py` file likely contains the main application logic, potentially using a framework like FastAPI or Streamlit. Run this file to start the chatbot:

    ```bash
    python app.py
    ```

    or

     ```bash
    streamlit run app.py
    ```

    Refer to the specific instructions within `app.py` for any required environment variables or configuration.

2.  **Interacting with the Chatbot:**

    The method for interacting with the chatbot will depend on how it's implemented in `app.py`.
    *   If it's a Streamlit app, access it through the URL provided after running `streamlit run app.py`.
    *   If it's a FastAPI backend, you might need to send requests to specific API endpoints defined in the code.
    *   The `query.py` script probably contains functions to make queries to the vector database and process the responses.

## Features

*   **Question Answering:** Answers user questions based on the provided knowledge base.
*   **ChromaDB Integration:** Uses ChromaDB for vector storage and retrieval, enabling efficient semantic search.
*   **Langchain Integration:** Leverages Langchain for building the chatbot and managing the conversational flow.
*   **API Support (Potentially):** May include an API built with FastAPI for programmatic access to the chatbot.
*   **Streamlit Interface (Potentially):** Offers a user-friendly interface built with Streamlit for easy interaction.
*   **Customizable Knowledge Base:** The knowledge base can be updated and expanded.

## Files and Structure

*   `.devcontainer/`: Contains configuration files for a development container (e.g., VS Code Dev Containers).
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `app.py`: Main application file, likely containing the chatbot's user interface (Streamlit) or API endpoints (FastAPI).
*   `chroma_db/`: Directory for ChromaDB related files, such as the persisted database.
*   `docs/`:  A place to put documentation for the project.
*   `main.py`: Might contain the core logic for setting up and running the chatbot.
*   `query.py`: Contains functions for querying the ChromaDB database and retrieving answers.
*   `requirements.txt`: Lists the Python packages required to run the project.

## Dependencies

The project uses the following main Python packages:

*   `langchain`: For building language model applications.
*   `chromadb`: As the vector database for storing and retrieving embeddings.
*   `fastapi`: For creating the API endpoints.
*   `streamlit`: For building the user interface.
*   `openai`: For using OpenAI's language models.

A complete list of dependencies can be found in the `requirements.txt` file.

## Additional Information
*   The .devcontainer folder provides a consistent development environment using Docker. If you're using VS Code, it can automatically configure your environment with all dependencies.
*   To use the OpenAI models, you will need an API key from OpenAI and set it as an environment variable (e.g., `OPENAI_API_KEY`). Check the `app.py` file for specific environment variable names.