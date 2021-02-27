# Importing the PIL library 
from PIL import Image, ImageFont, ImageDraw 
from datetime import date
import random

  
# Open an Image 
img = Image.open('certificate.png') #2000x1414
  
# Call draw Method to add 2D graphis in an image 
img_editable = ImageDraw.Draw(img) 
  
# Cutom font style and font size 
font = ImageFont.truetype("Roboto-Regular.ttf", 80)
  
name = "Irakli Maisuradze"
todays_date = str(date.today())
certinum = "C" + str(random.randint(100000, 999999))

# Add name to an image 
img_editable.text((1000, 500), name, anchor='ms', font = font, fill = (50, 50, 50)) 
# Add date to an image 
img_editable.text((1085, 967), todays_date, font = font, fill = (150, 150, 150)) 
# Add certinum to an image 
img_editable.text((1000, 800), certinum, anchor='ms', font = font, fill = (150, 150, 150)) 



# Save the edited image 
img.save("DigiHills Certificate for " + name + ".png") 
# img.save(certinum + ".png") 