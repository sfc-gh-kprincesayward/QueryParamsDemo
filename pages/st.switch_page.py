import streamlit as st

if st.button("ExperimentalQueryParams"):
    st.switch_page("./pages/ExperimentalQueryParams.py")
if st.button("Page 1"):
    st.switch_page("pages//test.py")
if st.button("Page 2"):
    st.switch_page("pages/widget_query_params.py")
