"""
Streamlit Interactive Plot
    
"""

import streamlit as st

st.title("Travel Emissions Calculator")
st.write("'It's a team, really: the wilderness and us.' \n\n — Per Espen Stoknes")
st.text("This app will allow you to enter vehicle miles traveled and tell you the CO2e emissions associated with your trip.")

options = st.multiselect(label = 'What modes of transportation did you use?', 
                         options = ['Personal vehicle', 'Bus (not including your own personal bus)', 'Flight', 'Rail', 'Boat']
                        )

st.write('You selected:', options)

if options == 'Personal vehicle':
   st.write("pass test") 
"""
    miles = st.number_input(label = "Insert the distance traveled in miles", min_value = 0, max_value = 10000)
st.write('The current distance is ', miles)
def emiss_calc(miles):
    co2 = miles * 404
    return co2

co2_g = emiss_calc(miles) 
co2_t = round((co2_g / 907200),3)




st.write('CO2 emissions for a',miles,'mi trip is',co2_g,'g or',co2_t,'tons.')
