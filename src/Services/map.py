from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageDraw, ImageFont


def generateMap ():
    # Create a map (size in pixels)
    m = StaticMap(600, 400)

    # Add a marker (longitude FIRST then latitude)
    marker = CircleMarker((153.032328, -27.464173), 'blue', 12)  # Tingalpa
    m.add_marker(marker)

    # Render the map to an image
    image = m.render(zoom=12, center=[153.117736, -27.474909])

    #image.save("map.png")

    ###adding registration number to map image
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    #define text (flight number)
    text = "QAN445" #to be replaced with plane RN
    text_x, text_y = 300, 200 #position in pixels (to change to lat/lon)

    #rectangle
    bbox = draw.textbbox((text_x, text_y), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    #draw rectangle 
    padding = 4
    box_coords = [
        (text_x - padding, text_y - padding),
        (text_x + text_w + padding, text_y + text_h + padding)
    ]
    draw.rectangle(box_coords, fill="white", outline="black")
    draw.text((text_x, text_y), text, font=font, fill="black")

    image.save("map.png")
    image.show()