from staticmap import StaticMap, CircleMarker


def generateMap ():
    # Create a map (size in pixels)
    m = StaticMap(600, 400)

    # Add a marker (longitude FIRST then latitude)
    marker = CircleMarker((153.032328, -27.464173), 'blue', 12)  # Tingalpa
    m.add_marker(marker)

    # Render the map to an image
    image = m.render(zoom=12, center=[153.117736, -27.474909])

    image.save("map.png")