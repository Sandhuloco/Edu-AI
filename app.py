import streamlit as st
import requests
from io import BytesIO

hide_streamlit_style = """
    <style>
    # MainMenu {visibility: hidden;}
    # footer {visibility: hidden;}
    # header {visibility: hidden;}
    </style>
    """

st.set_page_config(
    page_title="PDF-SUMMARIZER",
    layout="centered"
)

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("PDF Summarizer")

fileUpload = st.file_uploader("Upload a PDF file", type="pdf")

if st.button("Upload PDF"):
    if fileUpload is not None:
        with st.spinner('Loading...'):
            files = {"pdf_file": fileUpload.getvalue()}

            try:
                response = requests.post("http://127.0.0.1:8000/summarize/", files=files)

                if response.status_code == 200:
                    data = response.json()
                    if data["summaries"]:
                        st.subheader("Summary:")
                        st.text("\n".join(data["summaries"]))
                    else:
                        st.warning("No summaries available.")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please upload a PDF file.")