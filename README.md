# Travel_emissions_calculator

Abstract:
    Emissions from travel are a major source of ghg emissions in Burning Man's ghg profile. To fix it, we must know it and track it. This project is a calculator for participants, staff an outside venders to use to track their emissoins. 

**Design:**  
This project will perform emissions calculations and report them in Streamlit.
It will calculate:   
- Personal vehicle emissions with input of miles traveled, number of passenger, vehicle mpg, (is there an emissions API I can link to?). Approximate idle time during arrival and exodus. 
- Flight emissions with input of departure city, layover cities, destination city. Airplane will be asked (which can be found in flight itinerary from booking company). If aiplane is unknown, a general one will be used based on average plane type for flight distance.
- Bus emissions based on starting point and arrival point
- Train emissions based on multiple choice of rail type (commuter, regional, etc..) and possibly distance. 
- Boat emissions based on boat type and distance
- Reported human powered emissions (bike etc.) would produce a celebration graphic  



**Data:**    
Data would be provided by user. If results can be submitted to a collective database, they will be collected and stored in a sql db or on aws.   

**Algorithms:**  
To perform calculations.. *

**Tools:**   
Back end: This project will use python and Jupyter notebooks. I will search for API's for lat long and emissions by vehicle data.
Front end: streamlit will be used for the UI

**Communications:**  
This will be shared to my github and the streamlit app [link](www.google.com) will be circulated. Eventually, hosting this calculator somewhere more stable, robust, dynamic than streamlit would be good. 

**MVP:**   
The minimum viable product for this project is an emissions calculation in streamlit based only on miles driven
