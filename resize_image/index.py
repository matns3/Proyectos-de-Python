#Create toolbox to edit images
from PIL import Image

#Load image
img = Image.open("wallpaper.jpg")
"""
Image.open = in the "Image" toolbox, use (.) the "open" tool to load image
"""

#Resize image
new = img.resize((400, 300))
"""
img.resize = resize the image that is in "img" variable
(400, 300) = tuple
"""

#Save the new image
new.save("new_wallpaper.jpg")
"""
new.save = save the new image that is in "new" variable
"""

#Print original and new size
print("Original size:", img.size)
print("New size:", new.size)
