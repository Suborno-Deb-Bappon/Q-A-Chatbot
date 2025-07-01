# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python. It leverages various libraries such as Langchain, ChromaDB, and OpenAI to provide intelligent and context-aware responses to user queries. The chatbot can be integrated with different data sources and customized for specific domains.

## Installation

To set up the project locally, follow these steps:

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

4.  **Set up environment variables:**

    Create a `.env` file in the project root and add the necessary environment variables. For example:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    # Add other necessary variables here
    ```

## Usage

1.  **Running the main application:**

    Execute the `main.py` script to start the chatbot.

    ```bash
    python main.py
    ```

2.  **Running the app:**
    Execute the `app.py` script to start the chatbot with streamlit interface.

    ```bash
    streamlit run app.py
    ```

3.  **Interacting with the Chatbot:**

    Once the application is running, you can interact with the chatbot through the command line or the Streamlit interface (if running app.py).  Ask questions related to the data source that has been provided or any general knowledge questions, depending on the configuration.

## Features

*   **Question Answering:** Provides answers to user questions based on the context and available data.
*   **Langchain Integration:** Utilizes Langchain for building and managing conversational AI applications.
*   **ChromaDB:** Uses ChromaDB for vector storage and retrieval, enabling efficient semantic search.
*   **OpenAI API:** Integrates with the OpenAI API to generate intelligent and human-like responses.
*   **Customizable:** Can be customized and extended to support different data sources and domains.
*   **Streamlit Interface(app.py):** Provides a simple Streamlit interface for interacting with the chatbot.

## Project Structure

*   `app.py`: Contains the Streamlit application code for the chatbot interface.
*   `chroma_db/`: Directory for ChromaDB related files (vector storage).
*   `docs/`: Directory for documentation files.
*   `main.py`: Main application script to run the chatbot from the command line.
*   `query.py`: Contains functions for querying the knowledge base and generating responses.
*   `requirements.txt`: Lists the Python dependencies for the project.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `.devcontainer/`: Contains configuration files for a development container environment.

## Dependencies

The project relies on the following main dependencies:

*   `langchain`: For building conversational AI applications.
*   `chromadb`: For vector database management.
*   `openai`: For accessing OpenAI's language models.
*   `streamlit`: For creating the chatbot user interface.
*   `python-dotenv`: For loading environment variables from a `.env` file.

A complete list of dependencies can be found in the `requirements.txt` file.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).