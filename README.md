# Q-A-Chatbot

## Project Overview

This project implements a Question-Answering Chatbot using Python. It leverages Langchain for language model integration, ChromaDB for vector storage, and Streamlit for creating an interactive user interface. The chatbot is designed to answer questions based on a given knowledge base.

## Features

*   **Question Answering:** Answers questions based on a provided knowledge base.
*   **Langchain Integration:** Uses Langchain to interact with language models (e.g., OpenAI).
*   **ChromaDB Vector Storage:** Employs ChromaDB for efficient storage and retrieval of document embeddings.
*   **Streamlit UI:** Provides a user-friendly interface for interacting with the chatbot.
*   **Persistent Chat History:** Uses streamlit-chat to maintain the conversation history, improving the conversational experience.
*   **Modular Design:** Separates concerns into `app.py` (UI), `main.py` (application logic), and `query.py` (query processing) for better maintainability.

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
