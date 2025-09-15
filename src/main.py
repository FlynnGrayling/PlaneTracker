from Tracker import get_states
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

    #data = get_states(params=params, username=username, password=password)

    # if data:
    #     print("Successful Get")
    #     print("API Response (JSON):")
    #     print(data)

    # Create a map (size in pixels)
    m = StaticMap(600, 400)

    # Add a marker (longitude FIRST then latitude)
    marker = CircleMarker((153.032328, -27.464173), 'blue', 12)  # Tingalpa
    m.add_marker(marker)

    # Render the map to an image
    image = m.render(zoom=12, center=[153.117736, -27.474909])

    image.save("map.png")

if __name__ == "__main__":
    main()
