import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread("20180807002350.jpg")
print(type(img1))
# 顯示圖片
cv2.imshow('My Image', img1)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()