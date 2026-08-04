#Create toolbox to work with images and videos
import cv2

#Load image
img = cv2.imread("wallpaper.jpg")
"""
.imread = load image
"""

#Change color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
"""
cvtColor = change color
img = change image in the "img" variable
cv2.COLOR_BGR2GRAY = gray
"""

#Save the new image
cv2.imwrite("wallpaper_gray.jpg", gray)
"""
imwrite = save the new image
gray = save the new image in the "gray" variable
"""

#Show image
cv2.imshow("Wallpaper Gray Color", gray)
"""
.imshow = show image
gray = show image in the "gray" variable
"""

#Keep window open until key press
cv2.waitKey(0)
"""
.waitKey = keep window open until key press
0 = wait indefinitely
"""
