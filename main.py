import streamlit as st
import random
import time
# Create a title for your app
st.title('Smart Energy Management')

# Create a 3x2 grid layout
row1 = st.columns(3, gap='large')
demo = 4
i = 1
# Add a button to each column
for row in row1:
    with row:
        st.markdown(f'### Room {i}')
        status1 = st.empty()
        status1.markdown(f'''**Current Status:**  
        **No. of people:** {demo}  
        **Power Consumption:** ''')
        if st.button(f'Button {i}'):
            st.success(f"Button {i} clicked")
    i += 1


# Create another row
row2 = st.columns(3, gap= 'large')

i = 4
for row in row2:
    with row:
        st.markdown(f'### Room {i}')
        status1 = st.empty()
        status1.markdown(f'''**Current Status:**  
        **No. of people:** {demo}  
        **Power Consumption:** ''')
        if st.button(f'Button {i}'):
            st.success(f"Button {i} clicked")
    i += 1


while True:
    demo = random.randrange(1, 10)
    status1.markdown(f'''**Current Status:**  
    **No. of people:** {demo}  
    **Power Consumption:** ''')
    time.sleep(1)