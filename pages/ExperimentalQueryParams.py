import streamlit as st

qp = st.experimental_get_query_params()
st.write(qp)
st.warning("Hello world")

# st.experimental_set_query_params(
#     show_map=True,
#     selected=["asia", "america"],
# )
