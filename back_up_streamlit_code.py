"""
Streamlit Interactive Plot
    
"""

import streamlit as st

st.title("Travel Emissions Calculator")
st.write("'It's a team, really: the wilderness and us.' \n\n — Per Espen Stoknes")
st.text("This app will allow you to enter vehicle miles traveled and \n\n tell you the CO2e emissions associated with your trip.")

options = st.multiselect(label = 'What modes of transportation did you use?', 
                         options = ['Personal vehicle', 'Bus (not including your own personal bus)', 'Flight', 'Rail', 'Boat']
                        )

st.write('You selected:', options)

import streamlit as st

# Function to calculate emissions for personal vehicle - car/SUV/truck
def calculate_personal_vehicle_emissions(fuel_type, fuel_efficiency, occupancy, distance_traveled, vehicle_age):
    # Emission factors in kg CO2e per mile for different fuel types
    EMISSION_FACTORS = {
        "gasoline": 19.6,  # Example values, actual values may vary
        "diesel": 22.2,
        "R99 renewable diesel": 18.8
    }
    
    emission_factor = EMISSION_FACTORS.get(fuel_type, 0)
    if emission_factor == 0:
        return 0
    
    emissions = (distance_traveled / fuel_efficiency) * occupancy * (emission_factor / 1000) * vehicle_age
    return emissions

# Streamlit app
st.title("CO2e Emissions Calculator")

vehicle_options = ["Personal Vehicle", "Plane", "Boat", "Commercial Bus", "Rail"]
selected_vehicle = st.selectbox("Select a vehicle type:", vehicle_options)

if selected_vehicle == "Personal Vehicle":
    personal_vehicle_options = ["car/SUV/truck", "RV", "bus"]
    selected_personal_vehicle = st.selectbox("Select a personal vehicle type:", personal_vehicle_options)
    
    if selected_personal_vehicle in ["car/SUV/truck", "RV"]:
        fuel_type = st.selectbox("Select fuel type:", ["gasoline", "diesel", "R99 renewable diesel", "other"])
        
        if fuel_type == "other":
            st.write("Sorry, at this time our calculator does not produce emissions calculations for other fuels.")
        else:
            fuel_efficiency = st.number_input("Enter vehicle fuel efficiency (miles per gallon):", min_value=0.1)
            occupancy = st.number_input("Enter passenger occupancy:", min_value=1, step=1)
            distance_traveled = st.number_input("Enter distance traveled (miles):", min_value=0.1)
            vehicle_age = st.number_input("Enter vehicle age (years):", min_value=0, step=1)
            
            if st.button("Calculate Emissions"):
                emissions = calculate_personal_vehicle_emissions(fuel_type, fuel_efficiency, occupancy, distance_traveled, vehicle_age)
                st.write(f"CO2e Emissions: {emissions:.2f} metric tons")
    
elif selected_vehicle == "Plane":
    # Add code to calculate plane emissions
    
elif selected_vehicle == "Boat":
    # Add code to calculate boat emissions
    
elif selected_vehicle == "Commercial Bus":
    # Add code to calculate commercial bus emissions
    
elif selected_vehicle == "Rail":
    # Add code to calculate rail emissions
