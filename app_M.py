import streamlit as st
import random

st.set_page_config(layout="wide")
st.title('Test Streamlit')

with st.container():
    st.write("MMMMMM")

container = st.container(border=True)
container.write("NNNNNN")
