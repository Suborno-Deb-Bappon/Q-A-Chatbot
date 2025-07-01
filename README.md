# Q-A-Chatbot

## Overview

This project implements a Question-Answering Chatbot using Python, leveraging various libraries for natural language processing, vector storage, and API interactions. It provides a framework for building a chatbot that can answer questions based on a given knowledge base.

## Features

*   **Question Answering:** Answers questions based on a provided knowledge base.
*   **ChromaDB Integration:** Utilizes ChromaDB for vector storage and similarity search.
*   **Langchain Integration:** Uses Langchain for building the chatbot framework.
*   **OpenAI API:** Leverages the OpenAI API for generating responses.
*   **Streamlit Interface:** Provides a simple user interface using Streamlit for easy interaction.
*   **Asynchronous operations:** Uses asyncio and aiohttp for asynchronous tasks, allowing for better performance.

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

    You need to set your OpenAI API key as an environment variable. You can do this by creating a `.env` file in the project root directory:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

    Or by setting the environment variable directly in your terminal:

    ```bash
    export OPENAI_API_KEY=YOUR_OPENAI_API_KEY # Linux/macOS
    set OPENAI_API_KEY=YOUR_OPENAI_API_KEY # Windows
    ```

## Usage

1.  **Run the main script:**

    ```bash
    python main.py
    ```

    This script likely handles the initial setup or data processing for your chatbot.

2.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    This command will start the Streamlit application, and you can access it in your web browser at the address displayed in the terminal (usually `http://localhost:8501`).

## Project Structure

*   `app.py`: Contains the Streamlit application code for the chatbot interface.
*   `chroma_db`: Likely contains files related to the ChromaDB vector database setup.
*   `docs`: May contain documentation files.
*   `main.py`: Contains the main script for running the chatbot setup.
*   `query.py`: Includes functions and classes for querying the knowledge base and generating responses.
*   `requirements.txt`: Lists all the required Python packages.
*   `.devcontainer`: Contains configuration for a development container (VS Code).
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__`: Python cache directory

## Dependencies

The project uses the following main dependencies:

*   `langchain`: For building the chatbot framework.
*   `chromadb`: For vector storage and similarity search.
*   `openai`: For accessing the OpenAI API.
*   `streamlit`: For creating the user interface.
*   `python-dotenv`: For loading environment variables from a `.env` file.

A full list of dependencies can be found in `requirements.txt`.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is open-source and available under the [MIT License](LICENSE).