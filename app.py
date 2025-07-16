import streamlit as st
from summarizer import generate_summary

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📄 AI-Powered Text Summarizer")
st.write("Summarize lengthy articles in seconds using NLP.")

input_text = st.text_area("Paste your article or paragraph below:", height=300)

min_len = st.slider("Minimum Summary Length", 30, 200, 30)
max_len = st.slider("Maximum Summary Length", min_len + 10, 400, 120)

if st.button("Generate Summary"):
    if input_text.strip():
        with st.spinner("Summarizing..."):
            summary = generate_summary(input_text, min_len, max_len)
            st.subheader("📝 Summary")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
