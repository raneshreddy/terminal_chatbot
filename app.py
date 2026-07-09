import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("DSA Study Buddy")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a DSA tutor specializing in C++. When a user shares a problem, give hints only — never the full solution unless explicitly asked. When explaining concepts, always include a simple example. When reviewing code, point out time and space complexity."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

if prompt := st.chat_input("Ask me anything about DSA..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    ai_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    
    with st.chat_message("assistant"):
        st.write(ai_reply)