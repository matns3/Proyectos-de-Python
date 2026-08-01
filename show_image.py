#----------------------IMPORT----------------------
#Create toolbox to work with pictures and video
import cv2

#----------------------IMAGE----------------------
#Load image
img = cv2.imread("wallpaper.jpg")
"""
.imread() = load image
cv2.imread() = in the cv2 toolbox, use (.) the imread tool
"""

#Show image
cv2.imshow("Wallpaper", img)
"""
.imshow() = show image
cv2.imread() = in the cv2 toolbox, use (.) the imread tool
img = show image loaded in the "img" variable
"""

#Keep window open until key press
cv2.waitKey(0)
"""
waitKey = keep window open until key press
cv2.waitKey = in the cv2 toolbox, use "." the waitKey tool
0 = wait indefinitely
"""

#Close window
cv2.destroyAllWindows()
"""
destroyAllWindows() = close window
cv2.destroyAllWindows() = in the cv2 toolbox, use (.) the destroyAllWindow tool
"""