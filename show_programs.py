import streamlit as st
from java_programs import code_string_palindrome, code_reverse_string, code_reverse_array,code_recursion,code_binary_search,code_linear_search,code_insertion_sort

def app():
    st.title("Basic Programs Collection")
    st.header("Java Programs")
    with st.expander("Check if a String is Palindrome"):
        st.code(code_string_palindrome,language='python')


    with st.expander("Reverse a String"):
        st.code(code_reverse_string,language='python')

    with st.expander("Reverse an Array"):
        st.code(code_reverse_array,language='python')

    with st.expander("Program on Recursion"):
        st.code(code_recursion,language='python')

    with st.expander("Binary Search"):
        st.code(code_binary_search,language='python')

    with st.expander("Linear Search"):
        st.code(code_linear_search,language='python')

    with st.expander("Insertion Sort"):
        st.code(code_insertion_sort,language='python')
