from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd7in5_V2 #e-ink display driver, to be installed on raspberry pi (follow read me)
from datetime import datetime, timezone, timedelta

#Initialize recent_flight as a global variable
recent_flight = []

def generateHistory(flights, displayHistory):
    #initialise display
    epd = epd7in5_V2.EPD()

    #recent history list
    global recent_flight

    for plane in flights:
        # Skip if callsign already exists
        if any(plane[0] == records[0] for records in recent_flight):
            continue

        #convert unix time to AEST 
        AEST = timezone(timedelta(hours = 10))
        aest_time = datetime.fromtimestamp(plane[6], AEST)

        #format time display
        aest_time_formatted = aest_time.strftime("%I:%M:%S %p")

        #Insert Callsign, Origin, and Time from flights
        recent_flight.insert(0, (plane[0], plane[5], aest_time_formatted))

        #Shorten list if it is longer than 5
        if len(recent_flight) > 5:
            recent_flight = recent_flight[:5]
    
    print(recent_flight)

    #Image settings
    cell_widths = [160, 400, 225]  #Widths for each column
    row_height = 66
    header_height = 80
    padding = 10

    #Calculate image size
    img_width = 800
    img_height = 480

    #Create blank white image
    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    #Load font (fallback to default if not available)
    try:
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
        cell_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
        cell_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except:
        header_font = ImageFont.load_default(30)
        cell_header = ImageFont.load_default(30)
        cell_font = ImageFont.load_default(26)

    #Helper function to get text width & height from bbox
    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    #Draw title
    title = "Recent Flights"
    title_w, title_h = get_text_size(title, header_font)
    draw.text(((img_width - title_w) / 2, 10), title, font=header_font, fill="black")

    #Draw callsign rows
    y_increment = [0, 65, 130, 195, 260, 325, 390] #[0, 55, 110, 165, 220, 275, 330]
    x = 6
    y = 55
    x1 = 165
    x2 = 562
    for i in range(6):
        draw.rectangle([x, y + y_increment[i], x + cell_widths[0], y + row_height + y_increment[i]], outline="black", width=3)
        draw.rectangle([x1, y + y_increment[i], x1 + cell_widths[1], y + row_height + y_increment[i]], outline="black", width=3)
        draw.rectangle([x2, y + y_increment[i], x2 + cell_widths[2], y + row_height + y_increment[i]], outline="black", width=3)

    #Table headers
    headers = ["Callsign", "Departure Country", "Time"]
    
    #Header text
    header_x_pos = [25, 200, 625]
    for i, header in enumerate(headers):
        draw.text([x + header_x_pos[i], y + 15], header, font=cell_header, fill="black")

    #API Text
    data_x_pos = [25, 190, 600]
    data_y_pos = [140, 205, 270, 335, 400]
    for i, plane in enumerate(recent_flight):
        callsign = plane[0]
        origin = plane[1]
        time = plane[2]
        draw.text([x + data_x_pos[0], data_y_pos[i]], callsign, font=cell_font, fill="black")
        draw.text([x + data_x_pos[1], data_y_pos[i]], origin, font=cell_font, fill="black")
        draw.text([x + data_x_pos[2], data_y_pos[i]], str(time), font=cell_font, fill="black")

    #Save image and display image when appropriate
    if displayHistory == True:
        #convert image to B&W
        img.convert('1')

        #initialise and cleaar screen if History is to be shown
        epd.init()
        epd.Clear()

        epd.display(epd.getbuffer(img))
        epd.sleep()