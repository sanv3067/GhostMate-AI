
import streamlit as st
import requests

st.set_page_config(
    page_title="GhostMate AI",
    page_icon="👻",
    layout="centered"
)

st.title("👻 GhostMate AI")
st.caption("Your spooky stories, powered by local AI.")

st.markdown(
    "### 🕯️ Enter the world of forgotten mysteries..."
)

story_type = st.selectbox(
    "Choose your ghostly experience",
    [
        "Ghost Story",
        "Haunted Terminal",
        "Forgotten Memory Tale"
    ]
)

topic = st.text_area(
    "Enter a topic or idea",
    placeholder="Example: A mysterious message at midnight..."
)

if st.button("👻 Summon the Ghost", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        prompt = f"""
        You are GhostMate, a creative spooky storyteller.
        Create an original, engaging and atmospheric response.
        Experience type: {story_type}
        Topic: {topic}
        Keep the response suitable for a general audience.
        """

        with st.spinner("The ghost is awakening..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "gemma3:1b",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=180
                )
                response.raise_for_status()
                result = response.json()["response"]

                st.markdown("### 📜 Your Ghostly Creation")
                st.write(result)

            except requests.exceptions.RequestException as error:
                st.error(
                    "Could not connect to Ollama. "
                    "Check that Ollama is running."
                )
                st.code(str(error))
