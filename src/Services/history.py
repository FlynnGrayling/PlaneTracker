from PIL import Image, ImageDraw, ImageFont

def generateHistory():
    # Example data (from API)
    flights = [
        {"Callsign": "QAZ477", "Departure Country": "Australia", "Time": "06:30am"},
        {"Callsign": "NAZ307", "Departure Country": "New Zealand", "Time": "12:30pm"},
        {"Callsign": "AA2071", "Departure Country": "America", "Time": "12:30pm"},
        {"Callsign": "NAZ307", "Departure Country": "New Zealand", "Time": "01:30pm"},
        {"Callsign": "NAZ307", "Departure Country": "New Zealand", "Time": "09:30pm"},
    ]

    # Image settings
    cell_widths = [200, 300, 150]  # Widths for each column
    row_height = 60
    header_height = 80
    padding = 10

    # Calculate image size
    img_width = sum(cell_widths) + 20
    img_height = header_height + len(flights) * row_height + 20

    # Create blank white image
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Load font (fallback to default if not available)
    try:
        header_font = ImageFont.truetype("arialbd.ttf", 28)
        cell_font = ImageFont.truetype("arial.ttf", 22)
    except:
        header_font = ImageFont.load_default()
        cell_font = ImageFont.load_default()

    # Helper function to get text width & height from bbox
    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Draw title
    title = "Past Flights"
    title_w, title_h = get_text_size(title, header_font)
    draw.text(((img_width - title_w) / 2, 10), title, font=header_font, fill="black")

    # Table headers
    headers = ["Callsign", "Departure Country", "Time"]

    x = 10
    y = header_height
    for i, header in enumerate(headers):
        draw.rectangle([x, y, x + cell_widths[i], y + row_height], outline="black", width=3)
        text_w, text_h = get_text_size(header, cell_font)
        draw.text((x + (cell_widths[i] - text_w) / 2, y + (row_height - text_h) / 2),
                header, font=cell_font, fill="black")
        x += cell_widths[i]

    # Table rows
    y = header_height + row_height
    for flight in flights:
        x = 10
        for i, key in enumerate(headers):
            draw.rectangle([x, y, x + cell_widths[i], y + row_height], outline="black", width=3)
            value = flight[key]
            text_w, text_h = get_text_size(value, cell_font)
            draw.text((x + (cell_widths[i] - text_w) / 2, y + (row_height - text_h) / 2),
                    value, font=cell_font, fill="black")
            x += cell_widths[i]
        y += row_height

    # Save image
    img.save("flights_table.png")
    img.show()