from PIL import Image
import os.path
import requests
import shutil

LIMIT = 250
directory = "Images"
#Checks for and creates directory for images
if not os.path.isdir(directory):
   os.mkdir(directory)
   
   
#Downloads and saves an image

#image_location = "https://live.staticflickr.com/5122/5264886972_3234d62748.jpg"
image_location = "https://live.staticflickr.com/2106/2207159142_8206ab6984.jpg"
file = "Images/test.jpg"

#Opens image
image = requests.get(image_location, stream = True)

#Checks for retrieval then saves the image
if image.status_code == 200:
   image.raw.decode_content = True
   with open(file, 'wb') as pic:
      shutil.copyfileobj(image.raw, pic)

#adjusts image to standard size
if os.path.exists(file):
   with Image.open(file) as pict:
      width, height = pict.size
      if width > height:
         div = float(width)/float(LIMIT)
         if div > 1.0:
            newheight = float(height)/float(div)
            repict = pict.resize((int(LIMIT), int(newheight)))
            picture = repict.save(file)
         
      else:
         div = float(height)/float(LIMIT)
         if div > 1.0:
            newwidth  = float(width)/float(div)
            repict = pict.resize((int(newwidth), int(LIMIT)))
            picture = repict.save(file)