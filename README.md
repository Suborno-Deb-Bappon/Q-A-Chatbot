# Q-A-Chatbot

## Overview

This project implements a Question-Answering Chatbot using Python. It leverages various libraries for natural language processing, vector storage, and building a user interface. The chatbot is designed to ingest documents, store them in a vector database (ChromaDB), and then answer questions based on the content of those documents. It uses Langchain for orchestrating the NLP pipeline and Streamlit for creating a simple chat interface.

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

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary packages, including:

    *   `aiohappyeyeballs`
    *   `aiohttp`
    *   `aiosignal`
    *   `altair`
    *   `annotated-types`
    *   `anyio`
    *   `asgiref`
    *   `attrs`
    *   `backoff`
    *   `bcrypt`
    *   `blinker`
    *   `build`
    *   `cachetools`
    *   `certifi`
    *   `charset-normalizer`
    *   `chroma-hnswlib`
    *   `chromadb`
    *   `click`
    *   `colorama`
    *   `coloredlogs`
    *   `dataclasses-json`
    *   `Deprecated`
    *   `distro`
    *   `durationpy`
    *   `fastapi`
    *   `filelock`
    *   `flatbuffers`
    *   `frozenlist`
    *   `fsspec`
    *   `gitdb`
    *   `GitPython`
    *   `google-auth`
    *   `googleapis-common-protos`
    *   `greenlet`
    *   `grpcio`
    *   `h11`
    *   `httpcore`
    *   `httptools`
    *   `httpx`
    *   `huggingface-hub`
    *   `humanfriendly`
    *   `idna`
    *   `importlib-metadata`
    *   `importlib_resources`
    *   `Jinja2`
    *   `jiter`
    *   `jsonpatch`
    *   `jsonpointer`
    *   `jsonschema`
    *   `jsonschema-specifications`
    *   `kubernetes`
    *   `langchain`
    *   `langchain-chroma`
    *   `langchain-community`
    *   `langchain-core`
    *   `langchain-openai`
    *   `langchain-text-splitters`
    *   `langsmith`
    *   `markdown-it-py`
    *   `MarkupSafe`
    *   `marshmallow`
    *   `mdurl`
    *   `mmh3`
    *   `monotonic`
    *   `mpmath`
    *   `multidict`
    *   `mypy-extensions`
    *   `narwhals`
    *   `numpy`
    *   `oauthlib`
    *   `onnxruntime`
    *   `openai`
    *   `opentelemetry-api`
    *   `opentelemetry-exporter-otlp-proto-common`
    *   `opentelemetry-exporter-otlp-proto-grpc`
    *   `opentelemetry-instrumentation`
    *   `opentelemetry-instrumentation-asgi`
    *   `opentelemetry-instrumentation-fastapi`
    *   `opentelemetry-proto`
    *   `opentelemetry-sdk`
    *   `opentelemetry-semantic-conventions`
    *   `opentelemetry-util-http`
    *   `orjson`
    *   `overrides`
    *   `packaging`
    *   `pandas`
    *   `Pillow`
    *   `posthog`
    *   `propcache`
    *   `protobuf`
    *   `pyarrow`
    *   `pyasn1`
    *   `pyasn1_modules`
    *   `pydantic`
    *   `pydantic_core`
    *   `pydeck`
    *   `Pygments`
    *   `Pympler`
    *   `PyPika`
    *   `pyproject_hooks`
    *   `pyreadline3`
    *   `python-dateutil`
    *   `python-dotenv`
    *   `pytz`
    *   `pytz-deprecation-shim`
    *   `PyYAML`
    *   `referencing`
    *   `regex`
    *   `requests`
    *   `requests-oauthlib`
    *   `requests-toolbelt`
    *   `rich`
    *   `rpds-py`
    *   `rsa`
    *   `shellingham`
    *   `six`
    *   `smmap`
    *   `sniffio`
    *   `SQLAlchemy`
    *   `starlette`
    *   `streamlit`
    *   `streamlit-chat`
    *   `sympy`
    *   `tenacity`
    *   `tiktoken`
    *   `tokenizers`
    *   `toml`
    *   `tornado`
    *   `tqdm`
    *   `typer`
    *   `typing-inspect`
    *   `typing_extensions`
    *   `tzdata`
    *   `tzlocal`
    *   `urllib3`
    *   `uvicorn`
    *   `validators`
    *   `watchdog`
    *   `watchfiles`
    *   `websocket-client`
    *   `websockets`
    *   `wrapt`
    *   `yarl`
    *   `zipp`
    *   `pysqlite3-binary`

4.  **Set up your OpenAI API key:**

    You'll need an OpenAI API key to use the chatbot.  Set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Or, you can set it in a `.env` file in the project root:

    ```
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    If using a `.env` file, make sure the `python-dotenv` package is installed and that your code loads the environment variables accordingly.  The provided code in `app.py` includes an example using `load_dotenv`.

## Usage

1.  **Run the `main.py` script to ingest documents (if needed):**

    This script is responsible for loading documents, splitting them into chunks, creating embeddings, and storing them in the ChromaDB vector store.  You may need to modify the script to point to your desired document files.

    ```bash
    python main.py
    ```

2.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    This will start the Streamlit application, and you can access it in your browser, typically at `http://localhost:8501`.

3.  **Interact with the Chatbot:**

    Use the chat interface in your browser to ask questions related to the documents you've ingested. The chatbot will use the vector store to find relevant information and generate an answer.

## Features

*   **Document Ingestion:**  The chatbot can ingest various types of documents (e.g., text files, PDFs - depending on how you configure `main.py`).
*   **Vector Storage (ChromaDB):**  Uses ChromaDB to store document embeddings, enabling efficient similarity search for relevant information.
*   **Language Model Integration (OpenAI):**  Leverages OpenAI's language models (e.g., GPT-3.5) to generate answers based on retrieved information.
*   **Chat Interface (Streamlit):**  Provides a user-friendly chat interface for interacting with the chatbot.
*   **Langchain Integration:** Uses Langchain to create chains that handle document loading, splitting, embedding, vectorstore management, and question answering.
*   **.env Support:** Includes support for loading API keys and other settings from a `.env` file for easy configuration.

## File Structure

*   `app.py`: Contains the Streamlit application code for the chat interface.
*   `main.py`: Contains the code for ingesting documents, creating embeddings, and storing them in ChromaDB.
*   `query.py`: (Likely contains) Code related to querying the ChromaDB vector store.
*   `requirements.txt`: Lists the Python dependencies required for the project.
*   `chroma_db/`: Directory where the ChromaDB vector store is persisted.
*   `docs/`:  A directory intended for storing documents to be ingested by the chatbot.
*   `.devcontainer/`: Configuration files for using the project in a development container.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__/`:  A directory that Python creates to store compiled bytecode files.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

[Optional: Add a license here]