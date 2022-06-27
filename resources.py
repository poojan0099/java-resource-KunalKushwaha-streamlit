import base64
import streamlit as st
import os

def app():
    st.title("Refer this amazing notes!!")
    path=r"E:\\python practice\\streamlit\\array_arraylist.pdf"
    assert os.path.isfile(path)
    with st.expander("Introduciton to Arrays and Arraylist:"):
        def show_pdf(file_path):
            with open(path,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf('array_arraylist.pdf')
