from Tracker import get_states
from Services import generateMap
from staticmap import StaticMap, CircleMarker

def main():
    # bounding box properties (fixed coordinates)
    lamin = -27.587055  # lower latitude
    lamax = -27.331283  # higher latitude
    lomin = 153.032749  # lower longitude
    lomax = 153.158092  # higher longitude

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
        callsigns = [state[1].strip() for state in data['states'] if state[1].strip() != ""]
        print(callsigns)

    generateMap(callSigns=callsigns)

if __name__ == "__main__":
    main()
