import cv2
import numpy as np
from matplotlib import pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式

img = cv2.imread('test21_3.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 直边界矩形拟合
img1 = img.copy()
x, y, w, h = cv2.boundingRect(cnt)
area = cv2.contourArea(cnt)
aspect_ratio = float(w)/h  # 长宽比
rect_area = w*h
extent = float(area)/rect_area  # 轮廓面积与边界矩形面积的比。
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area  # 轮廓面积与凸包面积的比。
cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)
text1 = 'Aspect Ration: ' + str(round(aspect_ratio, 4))
text2 = 'Extent:  ' + str(round(extent, 4))
text3 = 'Solidity: ' + str(round(solidity, 4))
cv2.putText(img1, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img1, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img1, text3, (10, 90), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

# 最小矩形拟合
img2 = img.copy()
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)  # 获得矩形角点
area = cv2.contourArea(box)
width = rect[1][0]
height = rect[1][1]
cv2.polylines(img2, [box], True, (0, 255, 0), 3)
text1 = 'Width: ' + str(int(width)) + ' Height: ' + str(int(height))
text2 = 'Rect Area: ' + str(area)
cv2.putText(img2, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img2, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)


plt.subplot(232), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)), plt.title('Rectangle')
plt.subplot(233), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title('Rectangle')

plt.show()
