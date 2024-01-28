import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import random
import time
# Create a title for app
st.title('IoT Enabled Energy Management System')
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
            switch_page(f"Room {i}")
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
            switch_page(f"Room {i}")
        statuses.append(status)
    i += 1

def update_status(room, cur_stat, num, temp, power):
    with open(f'data/{room + 1}.csv', 'r') as f:
        lines = f.readlines()
        if len(lines) <= 1:
            statuses[room].markdown(f'''**Current Status:** Not Connected  
            **No. of people:** N/A  
            **Temperature:** N/A  
            **Power Consumption:** N/A''')
        else:
            data = lines[-1].split(',')
            cur_stat = data[-2].strip()
            temp = data[-3].strip()
            num = data[-4].strip()
            statuses[room].markdown(f'''**Current Status:** {cur_stat}  
            **No. of people:** {num}  
            **Temperature:** {temp}  
            **Power Consumption:** N/A''')


while True:
    demo = random.randrange(1, 10)
    cs = random.choice(['ON', 'OFF'])
    for j in range(len(statuses)):
        update_status(j, cs, demo, 12, 18)
    time.sleep(1)