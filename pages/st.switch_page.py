import streamlit as st

if st.button("Duplicate Query Params Demo"):
    st.switch_page("pages/DuplicateQueryParamsDemo.py")
if st.button("ExperimentalQueryParams"):
    st.switch_page("./pages/ExperimentalQueryParams.py")
if st.button("Simple Widget Query Params"):
    st.switch_page("pages/SimpleWidgetQueryParams.py")
