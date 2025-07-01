# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python. It leverages various libraries for natural language processing, vector databases, and web application development to provide an interactive and informative experience. The chatbot can ingest documents, store them in a vector database (ChromaDB), and answer questions based on the content of those documents.

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

    This will install all necessary packages, including:

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
    *   `frozenslist`
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

4.  **Set up environment variables:**

    Create a `.env` file in the project root and add your OpenAI API key:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

## Usage

1.  **Run the main script:**

    ```bash
    python main.py
    ```

    This script likely handles document loading, embedding, and storing in the ChromaDB database. Examine the `main.py` file for specific functionalities related to data ingestion.

2.  **Run the query script:**

    ```bash
    python query.py
    ```

    This script probably allows you to query the ChromaDB database with questions and retrieve answers. See `query.py` for details on how to formulate queries.

3.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    This will start a Streamlit application in your browser, providing a user interface for interacting with the chatbot.

## Features

*   **Document Ingestion:** The chatbot can ingest text documents, likely by splitting them into chunks and creating embeddings.
*   **Vector Database:** Uses ChromaDB to store document embeddings for efficient similarity search.
*   **Question Answering:** Answers questions based on the content of the ingested documents using Langchain and OpenAI's models.
*   **Streamlit Interface:** Provides a user-friendly web interface for interacting with the chatbot.
*   **Customizable:** The code is structured in a modular way, allowing for customization of document loading, embedding, and querying processes.

## Project Structure

*   `app.py`: Contains the Streamlit application code for the chatbot interface.
*   `main.py`: Likely contains the logic for loading documents, creating embeddings, and populating the ChromaDB database.
*   `query.py`: Contains the logic for querying the ChromaDB database and retrieving answers.
*   `chroma_db`: A directory to store the ChromaDB database files.
*   `docs`: A directory to store the documents to be ingested by the chatbot.
*   `requirements.txt`: Lists the Python dependencies required for the project.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `.devcontainer`: Contains configuration for a development container environment.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the [insert license here] License.