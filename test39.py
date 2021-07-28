import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('002.jpg')
src =  cv2.resize(src, (750, 500))
img = src.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours), contours[100].shape, hierarchy)
print(cv2.moments(contours[100]))
print(cv2.contourArea(contours[100]))
draw = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

plt.subplot(311), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(313), plt.imshow(cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)), plt.title('image')
plt.show()
