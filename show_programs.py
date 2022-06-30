import streamlit as st
from java_programs import code_string_palindrome, code_reverse_string, code_reverse_array,code_recursion,code_binary_search,code_linear_search,code_insertion_sort,cyclic_sort,find_duplicate_number,all_star_patterns,quick_sort,merge_sort,count_zeros,fibo_recursion

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

    with st.expander("Cyclic Sort"):
        st.code(cyclic_sort,language='python')

    with st.expander("Quick Sort"):
        st.code(quick_sort,language='python')

    with st.expander("Merge Sort"):
        st.code(merge_sort,language='python')

    with st.expander("Find the Duplicate Numbers"):
        st.code(find_duplicate_number,language='python')

    with st.expander("All Star Patterns"):
        st.code(all_star_patterns,language='python')

    with st.expander("Count Zeros in a Number"):
        st.code(count_zeros,language='python')
    
    with st.expander("Fibonacci Series using Recursion"):
        st.code(fibo_recursion,language='python')