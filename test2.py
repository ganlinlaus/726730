import numpy as np
import cv2

img = cv2.imread("20180807002350.jpg")
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),-1)
cv2.putText(img, "GG", (384, 223), 2, 7, (0, 0, 0))
# 顯示圖片
cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()