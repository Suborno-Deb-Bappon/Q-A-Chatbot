# Q-A-Chatbot

## Project Overview

This project implements a Question-Answering chatbot using Python. It leverages several libraries for natural language processing, vector storage, and building a user interface. The core functionality involves creating a knowledge base from documents, embedding the content, and then querying this knowledge base to provide answers to user questions. The application is built with Streamlit for the front-end and utilizes ChromaDB for vector storage and retrieval. Langchain is employed to chain different language models and vector stores together.

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
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary packages listed in the `requirements.txt` file, including `streamlit`, `chromadb`, `langchain`, `openai`, and other dependencies.

## Usage

1.  **Set up your OpenAI API key:**

    You\'ll need an OpenAI API key to use the language models. Set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Or, you can set the API key directly in your `.env` file if you\'re using `python-dotenv`. Make sure to install python-dotenv first, and create a .env file in the root directory with the OPENAI_API_KEY variable defined.

2.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This command will start the Streamlit application, and it will open in your web browser.

3.  **Interact with the Chatbot:**

    Once the application is running, you can type your questions in the chat interface. The chatbot will use the configured knowledge base to generate answers. Initial document loading and embedding may take some time.

## Project Structure and Important Files

*   `app.py`: This file contains the Streamlit application code, which provides the user interface for the chatbot.
*   `query.py`: This file likely handles the querying logic for retrieving answers from the ChromaDB vector store. It interacts with the Langchain framework to formulate queries and retrieve relevant information.
*   `main.py`: Might be responsible for the initial setup, data loading, or any background processes needed.
*   `chroma_db/`: This directory is expected to contain the ChromaDB database files.
*   `docs/`: This directory is expected to contain any source documents for the chatbot to train on.
*   `requirements.txt`: Lists all the Python packages required to run the project.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `.devcontainer/`: Contains configuration for a development container, enabling reproducible development environments.

## Features

*   **Question Answering:** Provides answers to user questions based on a pre-built knowledge base.
*   **Streamlit Interface:** User-friendly web interface built with Streamlit.
*   **ChromaDB Integration:** Uses ChromaDB for efficient vector storage and retrieval.
*   **Langchain Framework:** Leverages Langchain for chaining language models and vector stores.
*   **OpenAI Integration:** Utilizes OpenAI\'s language models for generating responses.
*   **Customizable Knowledge Base:** The knowledge base can be extended by adding more documents to the `docs/` directory, allowing customization for specific domains.
*   **Persistent Storage:** ChromaDB provides persistent storage for embeddings, allowing efficient retrieval across sessions.

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). (Assuming a license is applicable and included in the repository, otherwise remove the statement).