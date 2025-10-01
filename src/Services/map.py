from staticmap import StaticMap, CircleMarker
from PIL import Image, ImageDraw, ImageFont


def generateMap (flights):
    # Create a map (size in pixels)
    m = StaticMap(600, 400)

    # Add a marker (longitude FIRST then latitude)
    marker = CircleMarker((153.085000, -27.500000), 'blue', 12)  # Tingalpa
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

    for plane in flights:

        #set name and pixel position
        text = plane[0]
        text_x = plane[3]
        text_y = plane[4]

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

    #save and show image
    image.save("map.png")
    image.show()