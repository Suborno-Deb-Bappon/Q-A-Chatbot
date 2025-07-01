# Q-A-Chatbot

## Overview

This project implements a Question-Answering chatbot using Python. It leverages various libraries, including Langchain, ChromaDB, and OpenAI, to provide intelligent and context-aware responses to user queries. The chatbot can be customized and extended with different data sources and models.

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

    This will install all necessary packages listed in the `requirements.txt` file, including:

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
    *    `pysqlite3-binary`

4.  **Set up environment variables:**

    Create a `.env` file in the project root and add your OpenAI API key:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

## Usage

1.  **Run the main application:**

    ```bash
    python main.py
    ```

    This command will start the chatbot application. The specific behavior depends on the implementation in `main.py`, but it generally involves loading data, setting up the Langchain components, and initializing the chat interface.

2.  **Interact with the chatbot:**

    The `app.py` likely contains the code for creating a user interface (possibly using Streamlit) for interacting with the chatbot. Refer to `app.py` to understand how to run the UI. If it's a Streamlit app, you'd typically run:

    ```bash
    streamlit run app.py
    ```

    Follow the instructions provided by the application to ask questions and receive answers.

## Features

*   **Question Answering:** Provides answers to questions based on the provided data.
*   **Context Awareness:** Leverages Langchain and ChromaDB to maintain context and provide relevant responses.
*   **Customizable:** Can be extended with different data sources, models, and user interfaces.
*   **Uses ChromaDB:** Employs ChromaDB for vector storage and efficient similarity search.
*   **OpenAI Integration:** Utilizes OpenAI's models for generating answers.
*   **Streamlit Interface:** The `app.py` suggests the presence of a Streamlit-based user interface.

## Project Structure

*   `.devcontainer/`: Contains configuration for a development container.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `app.py`: Likely contains the Streamlit application code for interacting with the chatbot.
*   `chroma_db/`: Directory for ChromaDB related files (e.g., the database itself).
*   `docs/`: Directory for documentation files (currently empty).
*   `main.py`: The main entry point of the application, responsible for initializing and running the chatbot.
*   `query.py`: Contains functions for querying the database and generating responses.
*   `requirements.txt`: Lists the Python packages required to run the project.
*   `__pycache__`: Contains compiled Python files.