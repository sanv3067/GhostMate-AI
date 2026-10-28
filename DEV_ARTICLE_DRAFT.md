# GhostMate AI 👻: Spooky Stories with Local Open-Weight AI

> Before publishing, replace the GitHub placeholder with your actual public repository URL and add a real screenshot or demo.

## What I built
GhostMate AI is a Python and Streamlit app that creates fictional ghost stories, haunted-terminal scenes, and memory-inspired tales. Users choose an experience, enter an idea, and generate a response with Gemma 3 1B through Ollama running locally.

## Why it fits “Ghost in the Machine”
The project explores the spooky side of computers and generative AI, including a haunted-terminal story mode. The model runs locally, so prompts are not sent by this app to a hosted AI API.

## Why open innovation matters
A locally running open-weight model gives users more control over where prompts are processed. After downloading the model, the app can generate stories offline when Ollama and the model are available locally. It avoids per-request hosted API charges, though the computer still uses electricity and storage.

## How it works
- **Python** runs the app logic.
- **Streamlit** provides the interface.
- **Ollama** serves the model locally.
- **Gemma 3 1B** generates the stories.

## Try it
1. Install Ollama and download `gemma3:1b`.
2. Install dependencies from `requirements.txt`.
3. Run `python -m streamlit run app.py`.
4. Enter a topic and click **Summon the Ghost**.

## Project repository
[Add your public GitHub repository URL here.]

## Demo
[Add a screenshot or short demo video here.]

## What I learned
This project helped me practise connecting a Python interface to a locally running open-weight language model and handling connection errors in a small AI app.

#devchallenge #hf26challenge #hacktoberfest #opensource #python #ai
