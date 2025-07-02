# Q-A-Chatbot

## Overview

This project implements a Question-Answering Chatbot using Python. It leverages various libraries such as Langchain, ChromaDB, and OpenAI to provide intelligent and context-aware responses to user queries. The chatbot is designed to process documents, store their embeddings in a vector database, and retrieve relevant information based on user questions.

## Features

- **Document Processing:** Ingests and processes various document types (e.g., text files, PDFs).
- **Vector Database:** Utilizes ChromaDB to store document embeddings for efficient similarity search.
- **Language Model Integration:** Employs OpenAI's language models to generate coherent and informative answers.
- **Streamlit Interface:** Provides a user-friendly interface for interacting with the chatbot.
- **Customizable:** Allows customization of language models, embedding models, and document sources.
- **Context-Aware Responses:** Generates responses based on the context of the ingested documents.

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

    -   You will need an OpenAI API key to use the language model.
    -   Set the `OPENAI_API_KEY` environment variable.  You can do this by creating a `.env` file in the project root:

        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        ```

        Alternatively, you can set it directly in your shell:

        ```bash
        export OPENAI_API_KEY=YOUR_OPENAI_API_KEY  # Linux/macOS
        set OPENAI_API_KEY=YOUR_OPENAI_API_KEY  # Windows
        ```

## Usage

1.  **Prepare your documents:**

    -   Place the documents you want the chatbot to learn from in the `docs` directory.

2.  **Run the `main.py` script to ingest documents and create the ChromaDB:**

    ```bash
    python main.py
    ```

    This script will:
    - Load documents from the `docs` directory.
    - Split the documents into chunks.
    - Generate embeddings for each chunk using the OpenAI embedding model.
    - Store the embeddings in ChromaDB in the `chroma_db` directory.

3.  **Run the `app.py` script to start the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This will open the chatbot interface in your web browser.

4.  **Interact with the chatbot:**

    -   Type your question in the input box and press Enter.
    -   The chatbot will retrieve relevant information from ChromaDB and generate an answer using the OpenAI language model.

## Project Structure

-   `app.py`: Contains the Streamlit application code for the chatbot interface.
-   `main.py`: Contains the code for ingesting documents, creating embeddings, and storing them in ChromaDB.
-   `query.py`: Contains the core logic for querying the ChromaDB and generating responses.
-   `docs/`: A directory where you should place the documents the chatbot will learn from.
-   `chroma_db/`: A directory where ChromaDB stores the vector database. This will be created when you run `main.py`.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
-   `requirements.txt`: Lists the Python packages required to run the project.
-   `.devcontainer/`: (Optional) Contains configuration files for a development container environment.

## Dependencies

The project relies on the following Python packages:

-   `aiohappyeyeballs`
-   `aiohttp`
-   `aiosignal`
-   `altair`
-   `annotated-types`
-   `anyio`
-   `asgiref`
-   `attrs`
-   `backoff`
-   `bcrypt`
-   `blinker`
-   `build`
-   `cachetools`
-   `certifi`
-   `charset-normalizer`
-   `chroma-hnswlib`
-   `chromadb`
-   `click`
-   `colorama`
-   `coloredlogs`
-   `dataclasses-json`
-   `Deprecated`
-   `distro`
-   `durationpy`
-   `fastapi`
-   `filelock`
-   `flatbuffers`
-   `frozenlist`
-   `fsspec`
-   `gitdb`
-   `GitPython`
-   `google-auth`
-   `googleapis-common-protos`
-   `greenlet`
-   `grpcio`
-   `h11`
-   `httpcore`
-   `httptools`
-   `httpx`
-   `huggingface-hub`
-   `humanfriendly`
-   `idna`
-   `importlib-metadata`
-   `importlib_resources`
-   `Jinja2`
-   `jiter`
-   `jsonpatch`
-   `jsonpointer`
-   `jsonschema`
-   `jsonschema-specifications`
-   `kubernetes`
-   `langchain`
-   `langchain-chroma`
-   `langchain-community`
-   `langchain-core`
-   `langchain-openai`
-   `langchain-text-splitters`
-   `langsmith`
-   `markdown-it-py`
-   `MarkupSafe`
-   `marshmallow`
-   `mdurl`
-   `mmh3`
-   `monotonic`
-   `mpmath`
-   `multidict`
-   `mypy-extensions`
-   `narwhals`
-   `numpy`
-   `oauthlib`
-   `onnxruntime`
-   `openai`
-   `opentelemetry-api`
-   `opentelemetry-exporter-otlp-proto-common`
-   `opentelemetry-exporter-otlp-proto-grpc`
-   `opentelemetry-instrumentation`
-   `opentelemetry-instrumentation-asgi`
-   `opentelemetry-instrumentation-fastapi`
-   `opentelemetry-proto`
-   `opentelemetry-sdk`
-   `opentelemetry-semantic-conventions`
-   `opentelemetry-util-http`
-   `orjson`
-   `overrides`
-   `packaging`
-   `pandas`
-   `Pillow`
-   `posthog`
-   `propcache`
-   `protobuf`
-   `pyarrow`
-   `pyasn1`
-   `pyasn1_modules`
-   `pydantic`
-   `pydantic_core`
-   `pydeck`
-   `Pygments`
-   `Pympler`
-   `PyPika`
-   `pyproject_hooks`
-   `pyreadline3`
-   `python-dateutil`
-   `python-dotenv`
-   `pytz`
-   `pytz-deprecation-shim`
-   `PyYAML`
-   `referencing`
-   `regex`
-   `requests`
-   `requests-oauthlib`
-   `requests-toolbelt`
-   `rich`
-   `rpds-py`
-   `rsa`
-   `shellingham`
-   `six`
-   `smmap`
-   `sniffio`
-   `SQLAlchemy`
-   `starlette`
-   `streamlit`
-   `streamlit-chat`
-   `sympy`
-   `tenacity`
-   `tiktoken`
-   `tokenizers`
-   `toml`
-   `tornado`
-   `tqdm`
-   `typer`
-   `typing-inspect`
-   `typing_extensions`
-   `tzdata`
-   `tzlocal`
-   `urllib3`
-   `uvicorn`
-   `validators`
-   `watchdog`
-   `watchfiles`
-   `websocket-client`
-   `websockets`
-   `wrapt`
-   `yarl`
-   `zipp`
-   `pysqlite3-binary`

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

[MIT](LICENSE)