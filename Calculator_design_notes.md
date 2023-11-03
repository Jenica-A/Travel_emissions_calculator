Planning for calculator:

Outline:    
Ok, so far our work points to basically needing fuel type and volume. From there we will use generalized emissions equations, as the distincitons between emissions from different types of vehicles is fairly immaterial. 
Stationary combustion and mobile combustion are the two broadest categories, from there fuel type.
For participant travel, we will ask for emissions per mile. When it comes to flights, it's a whole lot more complicated. 

Simplify has been the name of the game.

**Did your journey to the event have the same number of legs as your journey home?** Define leg as a portion of your travels that was different, logistically, than other portions of your trip. IE did you pick up a passenger? Use the ferry? Stay in a hotel?
  If the answer is no, just have them fill out the one way details, then double them. If yes, open a new question about the return trip.
  
**How many legs did your journey to BRC have?** ```Dropdown with multiple choice. Once selected, questionnaire populates with dropdown questions for each outbound leg ```    
**How many legs did your return trip have?** ``` Similar to above. Dropdown multiple choice response populates questionnaire with that number of home-bound legs ```    
**First leg travel to BRC mode of transportation** ``` Multiple choice drop down: road travel, rail travel, air travel, water travel ```    

| Mode of Travel | Vehicle Options | 
| ----------- | ----------- |   
| Car      | Title       |   
| Plane   | Text        |    
| RV      | Title       |   

Second leg to BRC
Third leg to BRC


Flights
Road-travel
Rail-travel


Should we include hotels?

These will be drop-down options that users can select, with subsequent questions containing more drop-downs and/or boxes for entering numerical values. 
On the back end, the model will take in these inputs and perform calculations. Results will be shown in the app.

Vehicle type:
  Plane
    First leg
      Type of plane
        Class of seat
          Distance
    Next leg (repeat until done)
      Type of plane
        Class of seat
          Distance
  Personal vehicle
    First leg
      Type of vehicle (car, SUV, truck (not freight or U Haul style), RV, bus)
        Fuel type
          Towing? (yes or no)
            Approx mpg
              Occupancy
                Vehicle year
                  Approx hours idling or in very slow traffic?
    Next leg (add legs until done and returned "home")
      Type of vehicle (car, SUV, truck (not freight or U Haul style), RV, bus)
        Fuel type
          Towing? (yes or no)
            Approx mpg
              Occupancy
                Vehicle year
                  Approx hours idling or in very slow traffic?
  
At the end, sum all of the above emissions. 
  Boat
  Rail
  Commercial Bus
  At the end, offer results based on other methods (Did you know if you took the rail, your trip would have emitted x co2? Burner express would have emitted Y CO2.




## Building on suggestions from ChatGPT
Creating a travel emissions calculator for Burning Man participants involves several steps to estimate the carbon dioxide equivalent (CO2e) emissions from their round trip journey, considering flight layovers and other modes of transportation. Here's an outline of the parts of the calculator and a summary of the Python code needed for each step:

1. **User Input and Setup:**
   - Collect user input for trip details:
     - Departure and destination locations
     - Mode of transportation (e.g., car, plane)
     - Number of travelers
     - Distance if driving or flight information if flying (e.g., direct flight or layovers)
   - Set up constants for emission factors (e.g., CO2e per mile for cars, flights, layovers).

   ```python
   # Collect user input
   departure_location = input("Enter departure location: ") #This is a good way for us to QC results
   destination_location = input("Black Rock City, NV") #Should other stops be named? Will lat and lon be relevant?
   mode_of_transportation = input("Enter mode of transportation (car, plane, rail, boat, moving truck, semi, bicycle, etc.): ")
   num_travelers = int(input("Enter the number of travelers: ")) #This will be tricky for planes. We can build in assumption of plane size based on flight distance
   distance = float(input("Enter the distance (in miles or equivalent): ")) #This needs to be more specific, distance of each leg. We can use haversine equation for flight distance if necessary
   ```

2. **Calculate Emissions for Each Leg:**
   - Calculate emissions for each leg of the journey (e.g., driving to the airport, each flight segment, layovers, driving to Burning Man).
   - Account for the number of travelers.

   ```python
   # Calculate emissions for each leg
   emissions_driving_to_airport = distance * emission_factor_car * num_travelers
   emissions_flight_segments = sum([distance_segment * emission_factor_flight for distance_segment in flight_distances])
   emissions_layovers = num_layovers * emission_factor_layover * num_travelers
   emissions_driving_to_event = event_distance * emission_factor_car * num_travelers
   ```

3. **Sum Total Emissions:**
   - Sum the emissions from all legs to get the total CO2e emissions for the round trip.

   ```python
   total_emissions = (emissions_driving_to_airport +
                      emissions_flight_segments +
                      emissions_layovers +
                      emissions_driving_to_event)
   ```

4. **Display Results:**
   - Present the calculated emissions to the user in a user-friendly format.

   ```python
   print(f"Total CO2e emissions for the round trip: {total_emissions} kg CO2e")
   ```
4a. **Data Import** 
    - Data is imported to mysql db hosted on AWS and authenticated to burning man profile
    
5. **Optional: Emission Offset Information:**
   - Provide information on emission offset programs or suggestions for reducing emissions.

   ```python
   offset_programs = get_offset_programs(destination_location)
   print("Consider offsetting your emissions with the following programs:")
   for program in offset_programs:
       print(program)
   ```

6. **Error Handling:**
   - Include error handling to handle invalid user input and edge cases.

   ```python
   try:
       # Input collection and calculations here
   except ValueError:
       print("Invalid input. Please enter valid numerical values.")
   ```

7. **Optional: Interactive UI (e.g., web app):**
   - If desired, create a graphical user interface (GUI) for a more user-friendly experience using libraries like Flask or Django.
