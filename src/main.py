from Tracker import get_states
from Tracker import plotCoords
from Services import generateMap
from Services import generateHistory
from staticmap import StaticMap, CircleMarker

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

    # Add your OpenSky Network credentials
    username = ""
    password = ""

    data = get_states(params=params, username=username, password=password)

    if data:
        print("Successful Get")
        print("API Response (JSON):")
        print(data)
        #callsigns = [state[1].strip() for state in data['states'] if state[1].strip() != "NoCallsign"]
        flights = [
            [state[1].strip(), state[6], state[5], 0, 0]
            for state in data['states']
            if state[1].strip() != "NoCallsign" and state[6] != "NoLat" and state[5] != "NoLon"
        ]
        print(flights)

    
    # generateHistory()

    #get flight lon and lat
    # lat = [state[6] for state in data['states'] if state[6] != "NoLat"]
    # lon = [state[5] for state in data['states'] if state[5] != "NoLon"]

    #testing
    # callsigns = "VOC290"
    # lat = -27.5
    # lon = 153

    #flight details for testing list, calsign, lat, lon, pixX, pixY
    # flights = [["VOC290", -27.44, 153.0, 0, 0],
    #            ["QAZ290", -27.5, 153.15, 0, 0]]
    
    
    for plane in flights:
        #convert lon/lat to pixelcoords
        plane[3], plane[4] = plotCoords(lat = plane[1], lon = plane[2])


    generateMap(flights)

if __name__ == "__main__":
    main()
