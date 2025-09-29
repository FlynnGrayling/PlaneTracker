rows, cols = 4, 6
pixel_width, pixel_height = 400, 600

latMin, latMax = -27.58, -27.42
lonMin, lonMax = 153, 153.17

def plotCoords (lat, lon):
    # Size of one cell in world coordinates
    cell_width = (latMax - latMin) / cols
    cell_height = (lonMax - lonMin) / rows

    # Find col/row index
    col = int((lat - latMin) / cell_width)
    row = int((lon - lonMin) / cell_height)

    # Clamp to valid grid
    col = min(max(col, 0), cols - 1)
    row = min(max(row, 0), rows - 1)

    # Pixel center
    px_center_x = (col + 0.5) * (pixel_width / cols)
    px_center_y = (row + 0.5) * (pixel_height / rows)

    return row, col, (px_center_x, px_center_y)