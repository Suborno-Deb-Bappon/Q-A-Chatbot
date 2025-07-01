# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python. It leverages various libraries for natural language processing, vector storage, and web application development to provide a conversational interface for querying information.

## Installation

To set up the project, follow these steps:

1.  Clone the repository:

    ```bash
    git clone https://github.com/Suborno-Deb-Bappon/Q-A-Chatbot.git
    cd Q-A-Chatbot
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Set up environment variables:**

    The project likely requires certain environment variables (e.g., OpenAI API key). Create a `.env` file in the project root and add the necessary variables. For example:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

    Make sure to install the `python-dotenv` package if you haven't already: `pip install python-dotenv`. The `app.py` or `main.py` scripts likely load these variables.

2.  **Running the chatbot:**

    The project contains `app.py` and `main.py`. Based on the contents of the files, you can probably run the chatbot using one of the following commands:

    ```bash
    python main.py
    ```

    or

    ```bash
    streamlit run app.py # if it's a streamlit application
    ```

    Refer to the specific script (`app.py` or `main.py`) for any command-line arguments or configuration options.

3.  **Interacting with the chatbot:**

    Once the application is running, you can interact with the chatbot through the command line or a web interface (if `app.py` uses Streamlit or a similar framework). Follow the instructions displayed in the console or web interface to ask questions and receive answers.

## Features

*   **Question Answering:** Answers questions based on provided data or knowledge base.
*   **ChromaDB Integration:** Utilizes ChromaDB for vector storage and similarity search to find relevant information.
*   **Langchain:** Uses Langchain for orchestrating the chatbot pipeline, including document loading, text splitting, and question answering.
*   **OpenAI API:** Leverages OpenAI's API for language model functionalities.
*   **Streamlit UI (Potential):** If `app.py` is used, the chatbot may have a web interface built with Streamlit.
*   **Customizable:** The project structure allows for customization of the data sources, language model, and user interface.

## Project Structure

*   `.devcontainer/`: Contains configuration files for a development container environment.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `app.py`: Likely contains the main application code, possibly using Streamlit for a web interface.
*   `chroma_db/`: Contains files related to ChromaDB, such as the vector database.
*   `docs/`: May contain documentation files.
*   `main.py`: An alternative entry point for running the chatbot. May be used for command-line interaction.
*   `query.py`: Contains code for querying the knowledge base and generating responses.
*   `requirements.txt`: Lists the Python packages required to run the project.

## Dependencies

The project uses the following main Python packages:

*   `langchain`: Framework for building language model applications.
*   `chromadb`: Vector database for storing and retrieving embeddings.
*   `openai`: OpenAI API client.
*   `streamlit`: (Potentially) Framework for creating web applications.
*   `fastapi`: For building APIs (if used).
*   `uvicorn`: ASGI server for running FastAPI applications.
*   `python-dotenv`: For loading environment variables from a `.env` file.

A complete list of dependencies can be found in the `requirements.txt` file.