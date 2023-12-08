import streamlit as st

st.experimental_set_query_params(
    show_map=True,
    selected=["asia", "america"],
)
st.write(qp)
st.warning("Hello world")

# st.experimental_set_query_params(
#     show_map=True,
#     selected=["asia", "america"],
# )
