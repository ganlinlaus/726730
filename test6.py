import cv2

#開圖
img1 = cv2.imread('003.png')

print(img1.shape)
print(img1[100,200])
print(img1.item(100,200,1))
# img1[200:400,300:700]=[255,0,0]
roi = img1[400:600,300:700]  
h,w,a =roi.shape
img1[100:300,600:1000] = roi
print(len(roi),len(roi[0]))
img1[10:10+h,10:10+w] = roi
print(img1.size)
#秀圖
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)