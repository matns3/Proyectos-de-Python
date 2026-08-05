#Create toolbox to edit image
from PIL import Image

#Load image
img = Image.open("wallpaper.jpg")

#Average color
average = img.resize((1,1)).getpixel(0,0)
"""
.getpixel = get RGB color values at that exact pixel position
"""

#Split RGB tuple into three separate variables
r, g, b = average
"""
Example: if I obtain average = (10, 20, 30), with those three variables I split as follows: r=10, g=20, b=30
"""

#Detect which color channel is strongest
if g < r > b:
  color = "Red predominates"
elif r < g > b:
  color = "Green predominates"
elif r < b > g:
  color = "Blue predominates"
else:
  color = "Mix / grayish"

#Print the predominant color
print(f"Average Color: R={r}, G={g}, B={b} -> {color})
