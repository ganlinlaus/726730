import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('001.jpg', 0)


sobel = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=5)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)




sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow("img", img)
cv2.imshow("sobel", sobel)
#cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)
cv2.imshow("sobelyxy", sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()