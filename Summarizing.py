import streamlit as st
from transformers import pipeline

# Page config
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #008080;'>📝 Text Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Summarize long text into a few key lines using a Hugging Face model!</p>", unsafe_allow_html=True)

# Input
text = st.text_area("📄 Enter long text here:", height=200, placeholder="Paste or type a long article or paragraph...")

# Button
if st.button("📌 Summarize"):
    if len(text.strip()) < 30:
        st.warning("⚠️ Please enter at least a few meaningful sentences.")
    else:
        # Use a faster model
        summarizer = pipeline("summarization", model="t5-small")
        summary = summarizer(text, max_length=200, min_length=100, do_sample=False)[0]['summary_text']
        st.success("✅ Summary:")
        st.write(summary)

        # Display original text
        st.write("📄 Original Text:")
        st.write(text)

        # Display word count
        word_count = len(text.split())
        st.write(f"📚 Word Count: {word_count}")

        # Display character count
        char_count = len(text)
        st.write(f"📝 Character Count: {char_count}")
