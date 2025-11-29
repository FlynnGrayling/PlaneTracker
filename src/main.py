from Tracker import get_states
from Tracker import plotCoords
from Services import generateMap
from Services import generateHistory
from Display import setImage
from staticmap import StaticMap, CircleMarker
import time

def main():
    # bounding box properties (fixed coordinates)
    lamin = -27.540000  # lower latitude
    lamax = -27.410000 # higher latitude
    lomin = 152.990000  # lower longitude
    lomax = 153.250000  # higher longitude

    #middle coord values for map title
    lamid = lamin + lamax / 2 #-27.500000
    lomid = lomin + lomax / 2 #153.085000

    # define query parameters as dictionary
    params = {
        "time": 0,
        "icao24": "",
        "lamin": lamin,
        "lomin": lomin,
        "lamax": lamax,
        "lomax": lomax,
    }

    #Map darkmode, toggle for white or black map, darkmode is on by default
    darkMode = True

    storedFlights = []  # Initialize before loop
    displayCount = 0

    while True:
        # #clear/ instantiate lists
        flights = []

        #call API
        data = get_states(params=params)

        

        #if response parse wanted data to Flights list
        if data:
            print("Successful Get")
            print("API Response (JSON):")
            print(data)
            states = data.get('states')
            #callsigns = [state[1].strip() for state in data['states'] if state[1].strip() != "NoCallsign"]
            #check if data has returned some states, if not show default image
            if states and isinstance(states, list) and len(states) > 0:
                flights = [
                    [state[1].strip(), state[6], state[5], 0, 0, state[2].strip(), state[3]]
                    for state in states
                    if state[1].strip() != "NoCallsign" 
                    and state[6] != "NoLat" 
                    and state[5] != "NoLon"
                ]
                print(flights)
            else:
                #if states is empty set default display
                displayCount = setImage(flights, displayCount, darkMode)
        
        for plane in flights:
            #convert lon/lat to pixelcoords
            plane[3], plane[4] = plotCoords(lat = plane[1], lon = plane[2])

        # Compare callsigns and positions instead of full lists
        current_callsigns = {plane[0]: (plane[1], plane[2]) for plane in flights}
        stored_callsigns = {plane[0]: (plane[1], plane[2]) for plane in storedFlights}
        
        if current_callsigns != stored_callsigns:
            print("Flight data changed - updating display")
            displayCount = setImage(flights, displayCount, darkMode)
        else:
            print("No changes detected")

        storedFlights = flights

        time.sleep(60)

if __name__ == "__main__":
    main()
