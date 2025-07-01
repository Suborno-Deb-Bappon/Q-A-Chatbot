# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python, Langchain, ChromaDB, and OpenAI. It allows users to ask questions and receive answers based on a given knowledge base. The chatbot leverages embeddings to find relevant information and generate responses.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Suborno-Deb-Bappon/Q-A-Chatbot.git
    cd Q-A-Chatbot
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up your OpenAI API key:

    You\'ll need an OpenAI API key to use the chatbot. You can set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Or, you can set it directly in the `app.py` or `query.py` file. However, setting it as an environment variable is the recommended approach.

## Usage

There are two primary ways to interact with the chatbot: through the Streamlit-based `app.py` or directly using `query.py`.

### Streamlit App (`app.py`)

1.  Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2.  Open the URL displayed in the console (usually `http://localhost:8501`) in your web browser.

3.  Enter your question in the chat interface and press Enter to receive an answer.

### Direct Query (`query.py`)

1.  Run the `query.py` script, potentially modifying it to load data or execute specific queries:

    ```bash
    python query.py
    ```

    *Note:* You will likely need to adapt the `query.py` script to suit your data source and querying needs. The provided `query.py` file might need adjustment depending on how you want to use the chatbot.

## Features

*   **Question Answering:** Answers questions based on a provided knowledge base.
*   **Langchain Integration:** Uses Langchain for building the chatbot and managing the language model interactions.
*   **ChromaDB:** Employs ChromaDB for storing and retrieving document embeddings. This allows for efficient similarity search and retrieval of relevant information.
*   **OpenAI API:** Leverages the OpenAI API (specifically, `gpt-3.5-turbo` or other suitable models) for generating answers.
*   **Streamlit Interface (app.py):** Provides a user-friendly web interface for interacting with the chatbot.
*   **Modular Design:** The code is structured into separate modules (`app.py`, `query.py`, potentially others in `docs` or `chroma_db`) for better organization and maintainability.
*   **Customizable:** The chatbot can be customized by modifying the code and configuration files. Data loading, prompt engineering, and model parameters can be adjusted.

## Project Structure

*   `.devcontainer/`: Contains configuration for a development container (if used).
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `app.py`: Implements the Streamlit web application for the chatbot interface.
*   `chroma_db/`: Likely contains files related to the ChromaDB database, such as scripts for creating or managing the database.
*   `docs/`: May contain documentation files or data sources for the chatbot.
*   `main.py`: May contain the main entry point for running the chatbot (though `app.py` also serves as an entry point through Streamlit).
*   `query.py`: Contains code for querying the knowledge base and generating answers. This file likely handles the core logic of interacting with Langchain and ChromaDB.
*   `requirements.txt`: Lists the Python packages required to run the project.

## Dependencies

The project uses the following main dependencies:

*   `langchain`: For building language model applications.
*   `chromadb`: For vector database storage.
*   `openai`: For accessing OpenAI models.
*   `streamlit`: For creating the web interface.

A full list of dependencies is available in the `requirements.txt` file.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

[Optional: Add a license if you wish to specify how others can use your code.]