"""
Streamlit Interactive Plot
    
"""

import streamlit as st


st.title("Travel Emissions Calculator")
st.write("'We can prepare ourselves, and our families for the changes we're seeing.. more words ' \n\n — Per Espen Stoknes")

st.text("This app will allow you to enter miles traveled and tell you CO2e emissions more words")

miles = st.number_input(label = "Insert the distance traveled in miles", min_value = 0, max_value = 5000)
st.write('The current distance is ', miles)
def emiss_calc(miles):
    co2 = miles * 404
    return co2

emiss_calc(miles)

st.write('CO2 emissions for a',miles,'mi trip is ',emiss_calc(miles),'g.')
