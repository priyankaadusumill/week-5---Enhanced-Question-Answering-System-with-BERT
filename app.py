
import streamlit as st
from transformers import pipeline

# Load the BERT Question Answering model
qa_pipeline = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# Streamlit UI
st.title("Question Answering System with BERT")
st.write("Enter a context and a question below, and BERT will try to answer it!")

# User input fields
context = st.text_area("Enter the context:", height=200)
question = st.text_input("Enter your question:")

# Process the input
if st.button("Get Answer"):
    if context and question:
        result = qa_pipeline({"context": context, "question": question})
        st.subheader("Answer:")
        st.write(result["answer"])
    else:
        st.warning("Please enter both a context and a question.")
