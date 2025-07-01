# Q-A-Chatbot

## Overview

This project is a Question-Answering chatbot built using Python and several powerful libraries. It leverages the capabilities of `langchain`, `chromadb`, `streamlit`, and `openai` to create an interactive experience where users can ask questions and receive relevant answers. The chatbot uses ChromaDB for vector storage and retrieval, Langchain for orchestrating the chatbot flow, Streamlit for the user interface, and OpenAI for generating responses.

## Features

-   **Interactive Chat Interface:** Utilizes Streamlit to provide a user-friendly chat interface.
-   **Language Model Integration:** Employs OpenAI\'s language models for generating intelligent and context-aware responses.
-   **Vector Database:** Uses ChromaDB for efficient storage and retrieval of document embeddings.
-   **Langchain Orchestration:** Uses Langchain to manage the flow of questions and answers, providing a structured approach to chatbot interactions.
-   **Document Processing:** Processes and indexes documents to provide answers based on the provided data.

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
    *Note:* The `requirements.txt` file is dynamically created from the analysis, as the original repository does not include the file. To create it manually for reproducibility, use `pip freeze > requirements.txt` after installing the dependencies mentioned in the next step.

    Alternatively, install the main dependencies directly:

    ```bash
    pip install langchain chromadb streamlit openai
    ```

4.  **Set up your OpenAI API key:**

    You\'ll need an OpenAI API key to use the language model. You can set it as an environment variable:

    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    Or, you can set it directly in your script, but it\'s not recommended for security reasons.

## Usage

1.  **Run the main application:**

    ```bash
    python main.py
    ```

    or

     ```bash
    streamlit run app.py
    ```

2.  **Interact with the Chatbot:**

    Once the application is running, you can access the Streamlit interface in your web browser. The chatbot interface allows you to ask questions and receive answers based on the information it has been trained on.

## Project Structure

-   `app.py`: Likely contains the Streamlit application code for the chatbot interface.
-   `main.py`: The main entry point for running the chatbot application. It might handle initialization, data loading, and interaction with the language model.
-   `query.py`: Contains code related to querying the ChromaDB database and retrieving relevant information.
-   `chroma_db/`: Directory where the ChromaDB database is stored.
-   `docs/`:  Directory for documentation (currently empty in analysis).
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
-   `.devcontainer/`: Contains configurations for development containers, which can help ensure a consistent development environment.

## Dependencies

The project relies on the following main libraries:

-   **langchain:** For managing and orchestrating the chatbot flow.
-   **chromadb:** For vector storage and retrieval.
-   **streamlit:** For creating the user interface.
-   **openai:** For accessing language models.

The full list of dependencies includes:

```
aiohappyeyeballs==2.4.4
aiohttp==3.11.11
aiosignal==1.3.2
altair==5.5.0
annotated-types==0.7.0
anyio==4.8.0
asgiref==3.8.1
attrs==24.3.0
backoff==2.2.1
bcrypt==4.2.1
blinker==1.9.0
build==1.2.2.post1
cachetools==5.5.0
certifi==2024.12.14
charset-normalizer==3.4.1
chroma-hnswlib==0.7.3
chromadb==0.5.0
click==8.1.8
colorama==0.4.6
coloredlogs==15.0.1
dataclasses-json==0.6.7
Deprecated==1.2.15
distro==1.9.0
durationpy==0.9
fastapi==0.115.6
filelock==3.16.1
flatbuffers==24.12.23
frozenset==1.5.0
fsspec==2024.12.0
gitdb==4.0.12
GitPython==3.1.44
google-auth==2.37.0
googleapis-common-protos==1.66.0
greenlet==3.1.1
grpcio==1.69.0
h11==0.14.0
httpcore==1.0.7
httptools==0.6.4
httpx==0.28.1
huggingface-hub==0.27.1
humanfriendly==10.0
idna==3.10
importlib-metadata==6.11.0
importlib_resources==6.5.2
Jinja2==3.1.5
jiter==0.8.2
jsonpatch==1.33
jsonpointer==3.0.0
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
kubernetes==31.0.0
langchain==0.2.17
langchain-chroma==0.2.0
langchain-community==0.2.5
langchain-core==0.2.43
langchain-openai==0.1.8
langchain-text-splitters==0.2.4
langsmith==0.1.147
markdown-it-py==3.0.0
MarkupSafe==3.0.2
marshmallow==3.25.1
mdurl==0.1.2
mmh3==5.0.1
monotonic==1.6
mpmath==1.3.0
multidict==6.1.0
mypy-extensions==1.0.0
narwhals==1.21.1
numpy==1.26.4
oauthlib==3.2.2
onnxruntime==1.20.1
openai==1.59.6
opentelemetry-api==1.27.0
opentelemetry-exporter-otlp-proto-common==1.27.0
opentelemetry-exporter-otlp-proto-grpc==1.27.0
opentelemetry-instrumentation==0.48b0
opentelemetry-instrumentation-asgi==0.48b0
opentelemetry-instrumentation-fastapi==0.48b0
opentelemetry-proto==1.27.0
opentelemetry-sdk==1.27.0
opentelemetry-semantic-conventions==0.48b0
opentelemetry-util-http==0.48b0
orjson==3.10.14
overrides==7.7.0
packaging==23.2
pandas==2.2.3
Pillow==9.5.0
posthog==3.7.5
propcache==0.2.1
protobuf==4.25.5
pyarrow==18.1.0
pyasn1==0.6.1
pyasn1_modules==0.4.1
pydantic==2.10.5
pydantic_core==2.27.2
pydeck==0.9.1
Pygments==2.19.1
Pympler==1.1
PyPika==0.48.9
pyproject_hooks==1.2.0
pyreadline3==3.5.4
python-dateutil==2.9.0.post0
python-dotenv==1.0.0
pytz==2024.2
pytz-deprecation-shim==0.1.0.post0
PyYAML==6.0.2
referencing==0.35.1
regex==2024.11.6
requests==2.32.3
requests-oauthlib==2.0.0
requests-toolbelt==1.0.0
rich==13.9.4
rpds-py==0.22.3
rsa==4.9
shellingham==1.5.4
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
SQLAlchemy==2.0.37
starlette==0.41.3
streamlit==1.24.0
streamlit-chat==0.1.1
sympy==1.13.3
tenacity==8.5.0
tiktoken==0.7.0
tokenizers==0.21.0
toml==0.10.2
tornado==6.4.2
tqdm==4.67.1
typer==0.15.1
typing-inspect==0.9.0
typing_extensions==4.12.2
tzdata==2024.2
tzlocal==4.3.1
urllib3==2.3.0
uvicorn==0.34.0
validators==0.34.0
watchdog==6.0.0
watchfiles==1.0.4
websocket-client==1.8.0
websockets==14.1
wrapt==1.17.1
yarl==1.18.3
zipp==3.21.0
pysqlite3-binary
```

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the [MIT License](LICENSE).