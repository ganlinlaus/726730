import cv2
#相对路径下读取图片
doge = cv2.imread('001.jpg')
#灰度化处理
grayImage = cv2.cvtColor(doge,cv2.COLOR_BGR2GRAY)
#cv2.imshow('GRAY',grayImage)

#二值化处理，低于阈值的像素点灰度值置为0；高于阈值的值置为参数3
ret,thresh1 = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)
cv2.imshow('BINARY',thresh1)


#大于阈值的像素点灰度值置为0；小于阈值置为参数3
ret,thresh2 = cv2.threshold(grayImage,127,200,cv2.THRESH_BINARY_INV)
cv2.imshow('BINARY_INV',thresh2)

#小于阈值的像素点灰度值不变，大于阈值的像素点置为该阈值
ret,thresh3 = cv2.threshold(grayImage,127,255,cv2.THRESH_TRUNC)
cv2.imshow('TRUNC',thresh3)

#小于阈值的像素点灰度值不变，大于阈值的像素点置为0,其中参数3任取
ret,thresh4 = cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO)
cv2.imshow('BINARY_TOZERO',thresh4)


#大于阈值的像素点灰度值不变，小于阈值的像素点置为0,其中参数3任取
ret,thresh5 = cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('BINARY_TOZERO_INV',thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()