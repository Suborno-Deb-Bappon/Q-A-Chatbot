# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python. It leverages various libraries, including Langchain, ChromaDB, and OpenAI, to provide intelligent responses to user queries based on a given knowledge base. The chatbot is built using FastAPI for serving the API and Streamlit for creating an interactive user interface.

## Installation

To set up the Q-A-Chatbot, follow these steps:

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

    You'll need an OpenAI API key to use the chatbot. Set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Or, if you're on Windows:

    ```bash
    set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Alternatively, you can set the API key directly in your `.env` file if you prefer using `python-dotenv`. Ensure your `.env` file is properly configured and loaded in your `app.py` or `main.py`.

## Usage

### Running the API (FastAPI)

To start the API using FastAPI, execute the following command:

```bash
uvicorn app:app --reload
```

This will start the FastAPI application, and you can access the API endpoints at `http://127.0.0.1:8000` (or the address shown in the console).

### Running the Streamlit UI

To launch the Streamlit user interface, run:

```bash
streamlit run app.py
```

This will open the chatbot interface in your web browser. You can then interact with the chatbot by typing your questions in the input field.

## Project Structure

The project structure is organized as follows:

*   `.devcontainer/`: Contains configuration files for development using VS Code Dev Containers.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__/`: Contains compiled Python bytecode files.
*   `app.py`: Contains the Streamlit application code for the chatbot UI. Handles user input and displays responses.
*   `chroma_db/`: (Potentially) stores ChromaDB data if configured for persistent storage.
*   `docs/`: Intended for documentation files (currently empty).
*   `main.py`: May contain the main application logic and API endpoints using FastAPI.
*   `query.py`: Implements the question answering logic, including interaction with the Langchain and ChromaDB libraries. Likely contains functions for querying the knowledge base and generating responses.
*   `requirements.txt`: Lists the Python packages required to run the project.

## Features

*   **Question Answering:** Provides answers to user questions based on a predefined knowledge base.
*   **Langchain Integration:** Uses Langchain for building and managing conversational AI models.
*   **ChromaDB:** Employs ChromaDB for storing and retrieving document embeddings.
*   **OpenAI API:** Leverages OpenAI's language models (e.g., GPT) for generating responses.
*   **FastAPI Backend:** Uses FastAPI to create a robust and efficient API.
*   **Streamlit UI:** Offers an interactive user interface built with Streamlit.
*   **Customizable:** The knowledge base and chatbot behavior can be customized by modifying the code and data.
*   **Persistent vector store (ChromaDB):** ChromaDB allows for the persistence of the vector embeddings, enabling faster retrieval of information compared to re-computing embeddings every time the application starts.

## Dependencies

The project relies on the following Python packages:

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

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [Specify License] License.