rows, cols = 4, 8
height, width = 480, 800

latMin, latMax = -27.58, -27.42
lonMin, lonMax = 153, 153.17

def plotCoords(lat, lon):
    # Size of one cell in world coordinates
    cell_width = (lonMax - lonMin) / cols    # longitude -> X (columns)
    cell_height = (latMax - latMin) / rows   # latitude -> Y (rows)

    # Column index from longitude
    col = int((lon - lonMin) / cell_width)

    # Row index from latitude (flip because y increases downward)
    row = int((latMax - lat) / cell_height)

    # Clamp to valid grid
    col = min(max(col, 0), cols - 1)
    row = min(max(row, 0), rows - 1)

    # Pixel center
    px_center_x = (col + 0.2) * (width / cols)
    px_center_y = (row + 0.5) * (height / rows)

    return px_center_x, px_center_y

