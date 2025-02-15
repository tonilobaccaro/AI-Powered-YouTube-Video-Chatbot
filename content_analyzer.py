from openai import OpenAI
import streamlit as st

def initialize_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def generate_response(prompt, transcript):
    client = OpenAI(api_key="")

    system_message = f"""
    You are an AI assistant that answers questions about a video transcript. 
    Here's the transcript:
    {transcript}
    
    Answer the user's questions based on this transcript. If the answer is not in the transcript, say so.
    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=2000
    )

    return response.choices[0].message.content

def chat_interface(transcript):
    initialize_chat()
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about the video"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = generate_response(prompt, transcript)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

