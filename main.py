import streamlit as st
from PIL import Image

# Create a title for your app
st.title('My App')

# Create a 3x2 grid layout
col1, col2, col3 = st.columns(3, gap='large')

# Add a button to each column
with col1:
    if st.button('Button 1'):
        st.success("Button 1 clicked")

with col2:
    if st.button('Button 2'):
        st.success("Button 2 clicked")

with col3:
    if st.button('Button 3'):
        st.success("Button 3 clicked")

# Create another row
row2 = st.columns(3, gap= 'large')

with row2[0]:
    a = st.text('Hello')
    if st.button('Button 4'):
        st.success("Button 4 clicked")

with row2[1]:
    if st.button('Button 5'):
        st.success("Button 5 clicked")

with row2[2]:
    if st.button('Button 6'):
        st.success("Button 6 clicked")
