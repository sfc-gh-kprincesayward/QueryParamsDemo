import streamlit as st

with st.expander("Click here to see the code:"):
    st.code("""
import streamlit as st
query_params = st.query_params
if "is_checked" not in st.session_state:
    st.session_state["is_checked"] = (
        query_params.get("is_checked", "False").lower() == "true"
    )
my_checkbox = st.checkbox("Example Checkbox", key="is_checked")
query_params.is_checked = my_checkbox
st.write(st.session_state)
    """)

query_params = st.query_params
if "is_checked" not in st.session_state:
    st.session_state["is_checked"] = (
        query_params.get("is_checked", "False").lower() == "true"
    )
my_checkbox = st.checkbox("Example Checkbox", key="is_checked")
query_params.is_checked = my_checkbox
st.write(st.session_state)
