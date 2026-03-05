import streamlit as st
from llm import ask_ai
from utils.pdf_reader import read_pdf
from prompts.prompts import (
    explanation_prompt,
    summary_prompt,
    quiz_prompt,
    flashcard_prompt,
)

from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Study Buddy", layout="wide")

st.title("📚 AI Study Buddy")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Explain Topic",
        "Summarize Notes",
        "Generate Quiz",
        "Create Flashcards",
        "Upload PDF Notes",
    ],
)

# Explain Topic
if menu == "Explain Topic":

    topic = st.text_input("Enter topic")

    if st.button("Explain"):

        with st.spinner("AI is thinking..."):

            prompt = explanation_prompt(topic)

            response = ask_ai(prompt)

        st.write(response)


# Summarize Notes
elif menu == "Summarize Notes":

    notes = st.text_area("Paste your notes")

    if st.button("Summarize"):

        with st.spinner("Generating summary..."):

            prompt = summary_prompt(notes)

            response = ask_ai(prompt)

        st.write(response)


# Quiz Generator
elif menu == "Generate Quiz":

    topic = st.text_input("Enter topic")

    if st.button("Generate Quiz"):

        with st.spinner("Creating quiz..."):

            prompt = quiz_prompt(topic)

            response = ask_ai(prompt)

        st.write(response)


# Flashcards
elif menu == "Create Flashcards":

    topic = st.text_input("Enter topic")

    if st.button("Generate Flashcards"):

        with st.spinner("Generating flashcards..."):

            prompt = flashcard_prompt(topic)

            response = ask_ai(prompt)

        st.write(response)


# PDF Upload
elif menu == "Upload PDF Notes":

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:

        text = read_pdf(uploaded_file)

        if st.button("Summarize PDF"):

            with st.spinner("Analyzing PDF..."):

                prompt = summary_prompt(text[:4000])

                response = ask_ai(prompt)

            st.write(response)