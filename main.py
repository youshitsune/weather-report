import requests
import streamlit as st
import io

st.write("""
        # Weather report
        """)
location = st.text_input("Type in your location")
response = requests.get(f"https://wttr.in/{location}?format='%l:+%c+%t'")
st.write(response.text)
