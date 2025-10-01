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

    # data = get_states(params=params, username=username, password=password)

    # if data:
    #     print("Successful Get")
    #     print("API Response (JSON):")
    #     print(data)
    #     callsigns = [state[1].strip() for state in data['states'] if state[1].strip() != "NoCallsign"]
    #     print(callsigns)

    
    # generateHistory()

    #get flight lon and lat
    # lat = [state[6] for state in data['states'] if state[6] != "NoLat"]
    # lon = [state[5] for state in data['states'] if state[5] != "NoLon"]

    #testing
    callsigns = "VOC290"
    lat = -27.5
    lon = 153.5

    #flight details list
    #flights = [["VOC290", -27.44, 152.1],
               #["QAZ290", -27.5, ]]

    #convert lon/lat to pixelcoords
    row, col, pixX, pixY = plotCoords(lat = lat, lon = lon)
    print(f"Coord ({lat},{lon}) → cell ({row},{col}), pixel center x then y ({pixX},{pixY})")

    generateMap(callSigns=callsigns, pixX=pixX, pixY=pixY )

if __name__ == "__main__":
    main()
