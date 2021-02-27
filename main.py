# Importing the PIL library 
from PIL import Image, ImageFont, ImageDraw 
from datetime import date
import random
import qrcode

# Variables
name = input("Name on certificate: ") #"Irakli Maisuradze"
todays_date = str(date.today())
certinum = "C" + str(random.randint(100000, 999999))
  
# Open an Image 
img = Image.open('certificate.png') # Size = 2000x1414
# Call draw Method to add 2D graphis in an image 
img_editable = ImageDraw.Draw(img) 
# Custom font style and font size 
font = ImageFont.truetype("Roboto-Regular.ttf", 80)


# Generate QR code for website
qr = qrcode.make("https://digihills.ge/certificate/" + certinum) 
img.paste(qr, (1500, 700)) # Paste qr on img on coordinates xy


# Add name to an image 
img_editable.text((1000, 500), name, anchor='ms', font = font, fill = (50, 50, 50)) # ((x, y), text, anchor to middle-base against xy, font, fill with color) 
# Add date to an image 
img_editable.text((1085, 967), todays_date, font = font, fill = (150, 150, 150)) 
# Add certinum to an image 
img_editable.text((1000, 800), certinum, anchor='ms', font = font, fill = (150, 150, 150)) 


# Save the edited image 
#img.save("DigiHills Certificate for " + name + ".png") 
img.save(certinum + ".png") 