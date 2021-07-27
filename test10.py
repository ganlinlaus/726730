import cv2 as cv
import numpy as np
img1 = cv.imread("006.jpg")
#img2 = cv.imread()
#cap = cv.VideoCapture(0)
#_, frame = cap.read()
# Convert BGR to HSV
hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv.bitwise_and(img1,img1, mask= mask)
cv.imshow('frame',img1)
cv.imshow('mask',mask)
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()
