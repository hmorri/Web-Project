import os.path
import requests
import shutil

directory = "Images"
#Checks for and creates directory for images
if not os.path.isdir(directory):
   os.mkdir(directory)
   
   
#Downloads and saves an image

image_location = "https://live.staticflickr.com/5122/5264886972_3234d62748.jpg"
file = "test.jpg"

#Opens image
image = requests.get(image_location, stream = True)

#Checks for retrieval then saves the image
if image.status_code == 200:
   image.raw.decode_content = True
   with open(file, 'wb') as pic:
      #saves in the local directory, be sure to move this to the images folder
      shutil.copyfileobj(image.raw, pic)
