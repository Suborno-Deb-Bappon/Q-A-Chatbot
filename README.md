# Q-A-Chatbot

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)

## Overview

This project implements a Question-Answering Chatbot using Python. It leverages several libraries, including Langchain, ChromaDB, and OpenAI, to provide a conversational interface for querying information. The chatbot is built with a focus on modularity, allowing for easy customization and integration with various data sources.

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

4.  **Set up environment variables:**

    *   Create a `.env` file in the project root.
    *   Add your OpenAI API key:

        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        ```

## Usage

1.  **Run the main application:**

    ```bash
    python main.py
    ```

    This command will start the chatbot application, which may involve indexing documents or loading data into the ChromaDB vector store.

2.  **Run the query interface:**

    ```bash
    python query.py
    ```

    This script provides an interface to interact with the chatbot and ask questions against the knowledge base.

3.  **Run the app:**
    ```bash
    python app.py
    ```
    This will start a Streamlit application that provides a user-friendly interface for interacting with the chatbot.

## Features

*   **Question Answering:** Answers questions based on the indexed data.
*   **ChromaDB Integration:** Utilizes ChromaDB for vector storage and retrieval, enabling efficient similarity searches.
*   **Langchain Integration:** Leverages Langchain for building conversational AI applications.
*   **OpenAI Integration:** Employs OpenAI's models for generating responses.
*   **Streamlit Interface:** A user-friendly web interface powered by Streamlit for easy interaction.
*   **.devcontainer Support**: Includes a `.devcontainer` directory for easy development using VS Code Dev Containers.

## File Structure

*   `app.py`: Contains the Streamlit application for the chatbot interface.
*   `main.py`: Contains the main application logic, including indexing and data loading.
*   `query.py`: Contains the query logic for interacting with the chatbot.
*   `requirements.txt`: Lists the project dependencies.
*   `chroma_db/`: Directory for ChromaDB related files.
*   `docs/`: Directory for documentation files.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__`: Contains compiled Python files.
*   `.devcontainer`: Contains configuration files for VS Code Dev Containers.