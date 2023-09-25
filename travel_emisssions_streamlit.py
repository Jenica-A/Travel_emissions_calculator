import streamlit as st

# Function to calculate emissions for personal vehicle - car/SUV/truck
def calculate_personal_vehicle_emissions(fuel_type, fuel_efficiency, occupancy, distance_traveled, vehicle_age):
    # Emission factors in kg CO2e per gal for different fuel types
    EMISSION_FACTORS = {
        "gasoline": 8.78,  # Example values, actual values may vary
        "diesel": 10.21,
        "R99 renewable diesel": 11.000 # This is not an accurate value. Also neec CH4 and NO2
    }
    emission_factor = EMISSION_FACTORS.get(fuel_type, 0)
    if emission_factor == 0:
        return 0
    
    emissions = (distance_traveled / fuel_efficiency) / occupancy * (emission_factor / 1000) * vehicle_age
    return emissions
    
def calculate_flight_emissions(aviation_fuel_type, av_fuel_efficiency, plane_occupancy, distance_flown, plane_age):
    # Emission factors in kg CO2e per mile for different fuel types
    flight_EMISSION_FACTORS = {
        "Aviation Gas": 20,  # !!!Placeholder values. Replace with actual values
        "Jet Fuel": 22,
        "Other": 22,
        "Not sure": 22
    }
    
    flight_emission_factor = flight_EMISSION_FACTORS.get(aviation_fuel_type, 0)
    if flight_emission_factor == 0:
        return 0
    
    flight_emissions = (distance_flown / av_fuel_efficiency) / plane_occupancy * (flight_emission_factor / 1000) * plane_age
    return emissions

# Streamlit app
st.title("CO2e Emissions Calculator")
st.write("'It's a team, really: the wilderness and us.' \n\n — Per Espen Stoknes")
st.text("This app will allow you to enter vehicle miles traveled and \n\n report to you the CO2e emissions associated with your travel. \n\n PLEASE NOTE: Results are not accurate IN THIS CURRENT STATE. \n\n Place-holder equations are used on the back-end while the app is being built.")

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
st.write("This is a work in progress. Numbers are not actual results.")

if selected_vehicle == "Plane":
    plane_options = ["Private", "Commercial", "Burner Express Air"]
    selected_plane = st.selectbox("Select a plane type:", plane_options)
    
    if selected_plane == "Private":
        aviation_fuel_type = st.selectbox("Select aviation fuel type:", ["Aviation Gas", "Jet Fuel", "Other", "Not sure"])
        
        if aviation_fuel_type == "other":
            st.write("Sorry, at this time our calculator does not produce emissions calculations for other fuels.")
        else:
            av_fuel_efficiency = st.number_input("Enter plane fuel efficiency (miles per gallon):", min_value=0.1)
            plane_occupancy = st.number_input("Enter passenger occupancy:", min_value=1, step=1)
            distance_flown = st.number_input("Enter distance flown (miles):", min_value=0.1)
            plane_age = st.number_input("Enter age of plane (years):", min_value=0, step=1)
            
            if st.button("Calculate Flight Emissions"):
                flight_emissions = calculate_flight_emissions(aviation_fuel_type, av_fuel_efficiency, plane_occupancy, distance_flown, plane_age)
                st.write(f"CO2e Emissions: {flight_emissions:.2f} metric tons")


