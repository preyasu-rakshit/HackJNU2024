import streamlit as st
import random
import time
# Create a title for app
st.title('Smart Energy Management')
st.markdown('<br>', unsafe_allow_html=True)
# Create a 3x2 grid layout
row1 = st.columns(3, gap='large')
demo = 4
i = 1
statuses = []
for row in row1:
    with row:
        st.markdown(f'### Room {i}')
        status = st.empty()
        status.markdown(f'''**Current Status:**  
        **No. of people:** {demo}  
        **Power Consumption:** ''')
        if st.button(f'Manage Room {i}'):
            st.success(f"Button {i} clicked")
        statuses.append(status)
    i += 1

st.markdown('<br>', unsafe_allow_html=True)
# Create another row
row2 = st.columns(3, gap= 'large')

i = 4
for row in row2:
    with row:
        st.markdown(f'### Room {i}')
        status = st.empty()
        status.markdown(f'''**Current Status:**  
        **No. of people:** {demo}  
        **Power Consumption:** ''')
        if st.button(f'Manage Room {i}'):
            st.success(f"Button {i} clicked")
        statuses.append(status)
    i += 1

def update_status(room, cur_stat, num, power):
    statuses[room].markdown(f'''**Current Status:** {cur_stat}  
    **No. of people:** {num}  
    **Power Consumption:** {power}''')

while True:
    demo = random.randrange(1, 10)
    cs = random.choice(['ON', 'OFF'])
    for j in range(len(statuses)):
        update_status(j, cs, demo, 12)
    time.sleep(1)