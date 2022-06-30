import pdfminer
from pdfminer.high_level import extract_pages
import streamlit as st
from io import BytesIO

# st.write(pdfminer.__version__)  

def app():
    st.write("Upload your notes in PDF format.")
    uploaded_file = st.file_uploader("Choose a file", "pdf")

    if uploaded_file is not None:
        byteObject = uploaded_file.getvalue()
        with open('temp.pdf', 'wb') as f:
            f.write(byteObject)
        
        # for page_layout in extract_pages(uploaded_file):
        #     for element in page_layout:
        #         st.write(element)
        st.write("Uploaded Successfully!")
    
