import streamlit as st  # แก้จาก steamlit เป็น streamlit
import random

st.title('Test Streamlit')
st.write('Hello World!')

if st.button('Generate Random Number'):
    random_number = random.randint(1, 100)
    # แก้จาก ramdom_number เป็น random_number ให้ตรงกับที่ประกาศไว้ข้างบน
    st.write(f'Random Number: {random_number}')
