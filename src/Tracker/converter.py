import math

def lonlat_to_pixel(lon, lat, zoom, tile_size=256):
    # Convert lat/lon to mercator projection
    sin_lat = math.sin(lat * math.pi / 180.0)

    # Number of tiles across at this zoom level
    n = 2.0 ** zoom

    # X coordinate in pixels
    x = (lon + 180.0) / 360.0 * n * tile_size

    # Y coordinate in pixels
    y = (0.5 - math.log((1 + sin_lat) / (1 - sin_lat)) / (4 * math.pi)) * n * tile_size

    return (x, y)