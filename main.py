import requests
import streamlit as st

st.write("# Weather report")
location = st.text_input("Type in your location")
response = requests.get(f"https://wttr.in/{location}?format='%l:+%c+%t'&m")
st.write(response.text)
