# 👻 GhostMate AI

A spooky story assistant powered by local AI.

GhostMate AI is a Python + Streamlit app that creates fictional ghost stories, haunted-terminal scenes, and memory-inspired tales using Gemma 3 1B through Ollama.

## Features
- 👻 Generate original ghost stories.
- 💻 Create fictional haunted-terminal scenes.
- 🕯️ Generate respectful fictional tales inspired by old objects or memories.
- 🔒 Use a locally running model rather than a hosted AI API from this app.

## Requirements
- Python 3.10+
- [Ollama](https://ollama.com/)
- Gemma 3 1B (`gemma3:1b`)

## Setup

### 1. Download the model
Install Ollama, then run:
```bash
ollama run gemma3:1b
```
Wait for the model to download. You can exit the prompt after it finishes.

### 2. Install Python dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### 3. Run the app
Make sure Ollama is running, then:
```bash
python -m streamlit run app.py
```
Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Why local open-weight AI?
GhostMate uses Gemma 3 1B through Ollama, allowing story generation on your computer. The app sends prompts to the local Ollama service, not a hosted AI API. After downloading the model, generation can work offline if Ollama and the model are available locally.

## Demo
Add a screenshot or short demo video of the working app before publishing your DEV article.

## Hacktoberfest
Challenge theme: **Ghost in the Machine**. Check the official challenge page for submission requirements and tags before publishing.

## License
MIT. See [LICENSE](LICENSE).
