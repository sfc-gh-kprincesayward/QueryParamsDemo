import streamlit as st
st.title("Query Params API Demo!")
st.markdown("[Download link for the streamlit wheel file](https://github.com/willhuang1997/QueryParamsDemo/blob/main/streamlit-1.28.1-py2.py3-none-any.whl)")

with st.expander("Click here to see the code:"):
    st.code("""
import streamlit as st
st.title("Duplicate Page for Query Params API Demo!")
st.markdown("[Download link for the streamlit wheel file](https://github.com/willhuang1997/QueryParamsDemo/blob/main/streamlit-1.28.1-py2.py3-none-any.whl)")

selected_options = st.selectbox("Select an option to set the query_param value:", options, format_func=lambda x: f"{str(type(x))}:  {str(x)}")

check_clear = st.button("Run this code: ```st.query_params.clear()```")
if check_clear:
    st.query_params.clear()

check_del_query_param = st.button(f"Run this code: ```del st.query_params.PARAM_1```")
if check_del_query_param:
    del st.query_params.PARAM_1

check_set_attr = st.button(f"Run this code: ```st.query_params.PARAM_1 = {selected_options}```")
if check_set_attr:
    st.query_params.PARAM_1 = selected_options

check_set_item = st.button(f"Run this code: ```st.query_params['PARAM_2'] = {selected_options}```")
if check_set_item:
    st.query_params['PARAM_2'] = selected_options

st.header("Current query params:")
st.write(st.query_params)

check_get_attr = st.button(f"Run this code: ```st.write(st.query_params.PARAM_1)```")
if check_get_attr:
    st.write(st.query_params.PARAM_1)

check_get_item = st.button(f"Run this code: ```st.write(st.query_params['PARAM_1'])```")
if check_get_item:
    st.write(st.query_params['PARAM_1'])

check_get_all = st.button(f"Run this code: ```st.write(st.query_params.get_all('PARAM_1'))```")
if check_get_all:
    st.write(st.query_params.get_all('PARAM_1'))

check_get = st.button(f"Run this code: ```st.write(st.query_params.get('PARAM_1'))```")
if check_get:
    st.write(st.query_params.get('PARAM_1'))

check_get_default = st.button(f"Run this code: ```st.write(st.query_params.get('PARAM_1', 'DEFAULT_VALUE'))```")
if check_get_default:
    st.write(st.query_params.get('PARAM_1', default='DEFAULT_VALUE'))
    """)

options = [
    42,                     # Integer
    3.14,                   # Float
    "Hello, Streamlit!",    # String
    True,                   # Boolean
    [1, 2, 3],              # List
    (4, 5, 6),              # Tuple
    {"key": "value"},       # Dictionary
    {7, 8, 9},              # Set
    ""                      # Empty string
]

selected_options = st.selectbox("Select an option to set the query_param value:", options, format_func=lambda x: f"{str(type(x))}:  {str(x)}")

check_clear = st.button("Run this code: ```st.query_params.clear()```")
if check_clear:
    st.query_params.clear()

check_del_query_param = st.button(f"Run this code: ```del st.query_params.PARAM_1```")
if check_del_query_param:
    del st.query_params.PARAM_1

check_set_attr = st.button(f"Run this code: ```st.query_params.PARAM_1 = {selected_options}```")
if check_set_attr:
    st.query_params.PARAM_1 = selected_options

check_set_item = st.button(f"Run this code: ```st.query_params['PARAM_2'] = {selected_options}```")
if check_set_item:
    st.query_params['PARAM_2'] = selected_options

st.header("Current query params:")
st.write(st.query_params)

check_get_attr = st.button(f"Run this code: ```st.write(st.query_params.PARAM_1)```")
if check_get_attr:
    st.write(st.query_params.PARAM_1)

check_get_item = st.button(f"Run this code: ```st.write(st.query_params['PARAM_1'])```")
if check_get_item:
    st.write(st.query_params['PARAM_1'])

check_get_all = st.button(f"Run this code: ```st.write(st.query_params.get_all('PARAM_1'))```")
if check_get_all:
    st.write(st.query_params.get_all('PARAM_1'))

check_get = st.button(f"Run this code: ```st.write(st.query_params.get('PARAM_1'))```")
if check_get:
    st.write(st.query_params.get('PARAM_1'))

check_get_default = st.button(f"Run this code: ```st.write(st.query_params.get('PARAM_1', 'DEFAULT_VALUE'))```")
if check_get_default:
    st.write(st.query_params.get('PARAM_1', default='DEFAULT_VALUE'))
