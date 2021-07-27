import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test17.png')
img1 = cv2.imread('test16.png')

kernel = np.ones((5, 5), np.uint8)  # 卷积核
kernel2 = np.ones((10, 10), np.uint8)  # 卷积核