import streamlit as st
import random

st.set_page_config(layout="wide")
st.title('Test Streamlit')

col1, col2 = st.columns([0.3, 0.7], border=True)
with col1.container():
    st.write("Container 1 @ Column 1")

cc2 = col2.container(height=150)
cc2.write("Container 2 @ Column 2")
