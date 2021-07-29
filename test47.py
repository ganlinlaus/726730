import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('002.jpg')
img = cv.resize(img, (700, 500))
color = ("b", "g", "r")

histr1 = cv.calcHist([img], [1], None, [256], [0, 256])


mask = np.zeros(img.shape[:2], np.uint8)
mask[0:200, 0:100] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)
histr2 = cv.calcHist(masked_img, [0], None, [256],[0, 256])

plt.subplot(221), plt.imshow(img, 'gray'), plt.title("Image1")
plt.subplot(222), plt.plot(histr1), plt.title("Histogram"), plt.xlim([0, 256]) 
plt.subplot(223), plt.imshow(masked_img), plt.title("Image2")
plt.subplot(224), plt.plot(histr2), plt.title("Histogram"), plt.xlim([0, 256]) 
plt.show()