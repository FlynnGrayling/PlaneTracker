from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageDraw, ImageFont
import time


def generateMap (flights):
    # Create a map (size in pixels)
    m = StaticMap(800, 480)

    # Add a marker for home (longitude FIRST then latitude)
    marker = CircleMarker((153.030000, -27.466500), 'black', 12)  # Tingalpa
    m.add_marker(marker)

    # Add a marker for Airport (longitude FIRST then latitude)
    marker = CircleMarker((153.11, -27.4165), 'black', 12)  # Tingalpa
    m.add_marker(marker)
    

    # Render the map to an image
    image = m.render(zoom=12, center=[153.117736, -27.474909])

    #image.save("map.png")

    ###adding registration number to map image
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arialbd.ttf", 16)
        font2 = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        font2 = ImageFont.load_default()

    #draw HOME Box
    #set name and pixel position
    text = "HOME"
    text_x = 120
    text_y = 185

    # Get text bounding box
    bbox = draw.textbbox((text_x, text_y), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # Draw rectangle
    padding = 4
    box_coords = [
        (text_x - padding, text_y - padding),
        (text_x + text_w + padding, text_y + text_h + padding)
    ]
    draw.rectangle(box_coords, fill="white", outline="black")

    # Draw text
    draw.text((text_x, text_y), text, font=font, fill="black")

    #draw AIRPORT Box
    #set name and pixel position
    text = "AIRPORT"
    text_x = 342
    text_y = 20

    # Get text bounding box
    bbox = draw.textbbox((text_x, text_y), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # Draw rectangle
    padding = 4
    box_coords = [
        (text_x - padding, text_y - padding),
        (text_x + text_w + padding, text_y + text_h + padding)
    ]
    draw.rectangle(box_coords, fill="white", outline="black")

    # Draw text
    draw.text((text_x, text_y), text, font=font, fill="black")

    for plane in flights:

        #set name and pixel position
        text = plane[0]
        text_x = plane[3]
        text_y = plane[4]

         # Get text bounding box
        bbox = draw.textbbox((text_x, text_y), text, font=font2)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
    
        # Draw rectangle
        padding = 4
        box_coords = [
            (text_x - padding, text_y - padding),
            (text_x + text_w + padding, text_y + text_h + padding)
        ]
        draw.rectangle(box_coords, fill="white", outline="black")

        # Draw text
        draw.text((text_x, text_y), text, font=font2, fill="black")

    #save and show image
    image.save("map.png")
    image.show()