from Tracker import get_states
from Tracker import plotCoords
from Services import generateMap
from Services import generateHistory
from Display import setImage
from staticmap import StaticMap, CircleMarker
import time

def main():
    # bounding box properties (fixed coordinates)
    lamin = -27.580000  # lower latitude
    lamax = -27.420000 # higher latitude
    lomin = 153.000000  # lower longitude
    lomax = 153.170000  # higher longitude

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

    #flight details for testing list, calsign, lat, lon, pixX, pixY, Origin, Time (Unix)
    # flights = [["VOC290", -27.44, 153.0, 0, 0, "Australia", 18000],
    #            ["VOC291", -27.48, 153.15, 0, 0, "Singapore", 27000],
    #            ["VOC292", -27.5, 153.12, 0, 0, "Brasil", 27000],
    #            ["VOC293", -27.54, 153.16, 0, 0, "England", 27000],
    #            ["VOC294", -27.56, 153.0, 0, 0, "New Zealand", 27000],
    #            ["VOC295", -27.5, 153.1, 0, 0, "Mexico", 27000],]


    # Add your OpenSky Network credentials
    username = ""
    password = ""

    storedFlights = []  # Initialize before loop
    displayCount = 0

    while True:
        # #clear/ instantiate lists
        flights = []

        #call API
        data = get_states(params=params, username=username, password=password)

        #if response parse wanted data to Flights list
        if data:
            print("Successful Get")
            print("API Response (JSON):")
            print(data)
            #callsigns = [state[1].strip() for state in data['states'] if state[1].strip() != "NoCallsign"]
            flights = [
                [state[1].strip(), state[6], state[5], 0, 0, state[2].strip(), state[3]]
                for state in data['states']
                if state[1].strip() != "NoCallsign" and state[6] != "NoLat" and state[5] != "NoLon"
            ]
            print(flights)
        
        for plane in flights:
            #convert lon/lat to pixelcoords
            plane[3], plane[4] = plotCoords(lat = plane[1], lon = plane[2])

        # Compare callsigns and positions instead of full lists
        current_callsigns = {plane[0]: (plane[1], plane[2]) for plane in flights}
        stored_callsigns = {plane[0]: (plane[1], plane[2]) for plane in storedFlights}
        
        if current_callsigns != stored_callsigns:
            print("Flight data changed - updating display")
            displayCount = setImage(flights, displayCount)
        else:
            print("No changes detected")

        storedFlights = flights

        time.sleep(60)

if __name__ == "__main__":
    main()
