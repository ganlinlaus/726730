import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('white.png')
img = cv.resize(img, (700, 500))
color = ("b", "g", "r")

histr = cv.calcHist([img], [1], None, [256], [0, 256])
plt.plot(histr, 'b')
plt.xlim([0, 256])

plt.show()