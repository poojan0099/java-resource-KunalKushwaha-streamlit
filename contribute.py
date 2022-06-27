import streamlit as st
import pandas as pd
import os
import docx2txt
import pdfplumber


def app():
    st.title("Contribute here!")
    st.markdown("Feel free to upload your notes, programs which will be reviewed and displayed on the app!")
    docx_file = st.file_uploader("Upload Document", type=["pdf","docx","txt"])

    if docx_file is not None:
        file_details = {"filename":docx_file.name, "filetype":docx_file.type,"filesize":docx_file.size}
        st.write(file_details)


    with open(os.path.join("files_upload",docx_file.name),"wb") as f:
        f.write((docx_file).getbuffer())

    st.success("File Saved")


