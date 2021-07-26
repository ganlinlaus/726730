import numpy as np
import cv2 as cv

import numpy as np
import cv2

def drawcircle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img1, (x, y), 100, (255, 0, 0), 3)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv.rectangle(img1,(x, y),(x + 30, y + 30),(0,255,0),3)

img1 = cv2.imread("20180807002350.jpg")
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image', drawcircle)
while(1):
    cv.imshow('image',img1)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
# 顯示圖片


