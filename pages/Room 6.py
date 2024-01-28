import streamlit as st
import time
import pandas as pd
import plotly.express as px
import requests
from url import url

# Create a title for app
st.markdown("<h1 style='text-align: center; color: white;'>Room 1</h1>", unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
# Create a 3x2 grid layout
row1 = st.columns(2, gap='large')
demo = 4
i = 1

df = pd.read_csv('data/6.csv')
df = df.sort_values(by=' time')

with row1[0]:
    st.markdown('### Manual Controls')
    status = st.empty()
    status.markdown(f'''**Current Status:**  
    **No. of people:** {demo}  
    **Power Consumption:** ''')
    if st.button('Toggle State'):
        requests.get(url)
        st.success(f"Toggled Succesfully")
    ac = st.slider('Set Thermostat', 16, 32, step=1)

with row1[1]:
    fig = px.line(df, x = ' time', y = 'count', title='No. of People v/s Time', height=350, labels={' time': 'Time', 'count': 'Count'})
    st.plotly_chart(fig, use_container_width=True)


st.markdown('<br>', unsafe_allow_html=True)
# Create another row
row2 = st.columns(2, gap= 'large')

with row2[0]:
    fig = px.line(df, x = ' time', y = ' temp', title='Temperature v/s Time', height=350)
    st.plotly_chart(fig, use_container_width=True)

with row2[1]:
    response_counts = df[' state'].value_counts()
    fig = px.pie(response_counts,labels=response_counts.index,values=response_counts.values,title='Up time / Down Time', height=350)
    st.plotly_chart(fig, use_container_width=True)

def update_status(room):
    with open(f'data/{room}.csv', 'r') as f:
        lines = f.readlines()
        if len(lines) <= 1:
            status.markdown(f'''**Current Status:** Not Connected  
            **No. of people:** N/A  
            **Temperature:** N/A  
            **Power Consumption:** N/A''')
        else:
            data = lines[-1].split(',')
            cur_stat = data[-2].strip()
            temp = data[-3].strip()
            num = data[-4].strip()
            status.markdown(f'''**Current Status:** {cur_stat}  
            **No. of people:** {num}  
            **Temperature:** {temp}  
            **Power Consumption:** N/A''')


while True:
    update_status(6)
    time.sleep(1)