import base64
import streamlit as st
import os

def app():
    st.title("Refer this amazing notes!!")
    path=r"E:\\python practice\\streamlit\\notes\\intro_to_java.pdf"
    assert os.path.isfile(path)
    with st.expander("Introduciton to Java"):
        def show_pdf(file_path):
            with open(path,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf('array_arraylist.pdf')


    path2=r"E:\\python practice\\streamlit\\notes\\First_Java_Program_Notes.pdf"
    assert os.path.isfile(path)
    with st.expander("First Java Program"):
        def show_pdf2(file_path):
            with open(path2,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf2('array_arraylist.pdf')

    path2=r"E:\\python practice\\streamlit\\notes\\Conditionals_And_Loops.pdf"
    assert os.path.isfile(path)
    with st.expander("Conditional ans Loops"):
        def show_pdf2(file_path):
            with open(path2,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf2('array_arraylist.pdf')

    path2=r"E:\\python practice\\streamlit\\notes\\functions_methods.pdf"
    assert os.path.isfile(path)
    with st.expander("Methods in Java"):
        def show_pdf2(file_path):
            with open(path2,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf2('array_arraylist.pdf')

    path1=r"E:\\python practice\\streamlit\\notes\\array_arraylist.pdf"
    assert os.path.isfile(path)
    with st.expander("Arrays and ArrayList in Java"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("array_arraylist.pdf")

    path1=r"E:\\python practice\\streamlit\\notes\\linear_search.pdf"
    assert os.path.isfile(path)
    with st.expander("Linear Search"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("linear_search.pdf")

    path1=r"E:\\python practice\\streamlit\\notes\\binary_search.pdf"
    assert os.path.isfile(path)
    with st.expander("Binary Search"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("linear_search.pdf")

    path1=r"E:\\python practice\\streamlit\\notes\\insertion_sort.pdf"
    assert os.path.isfile(path)
    with st.expander("Insertion Sort"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("linear_search.pdf")

    path1=r"E:\\python practice\\streamlit\\notes\\selection_sort.pdf"
    assert os.path.isfile(path)
    with st.expander("Selecction Sort"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("selection_sort.pdf")

    path1=r"E:\\python practice\\streamlit\\notes\\bubble_sort.pdf"
    assert os.path.isfile(path)
    with st.expander("Bubble Sort"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("bubble_sort.pdf")

    path1=r"E:\\python practice\\streamlit\\notes\\strings.pdf"
    assert os.path.isfile(path)
    with st.expander("Strings in Java"):
        def show_pdf1(file_path):
            with open(path1,"rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            pdf_display1 = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="670" height="750" type="application/pdf"></iframe>'
            st.markdown(pdf_display1, unsafe_allow_html=True)

        show_pdf1("strings.pdf")

    with st.expander("OOP in Java"):
        st.write("[Object Oriented Programming](https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/tree/main/lectures/17-oop/notes)")