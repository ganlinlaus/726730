import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    img = frame
    #img = cv2.resize(img1,None, fx=1/8,fy=1/8,interpolation=cv2.INTER_LINEAR)
    cv2.namedWindow('image')
    blur = cv2.GaussianBlur(img,(9,9),0)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    scharrx = cv2.Sobel(gray,cv2.CV_64F,1,0)
    scharry = cv2.Sobel(gray,cv2.CV_64F,0,1)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.convertScaleAbs(scharry)
    scharrxy = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
    edges1 = cv2.Canny(gray,50,150) 
    contours, hi = cv2.findContours(edges1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img1 = edges1
    newcountours=[]
    for contour in contours:
        if cv2.contourArea(contour) > 50 and cv2.arcLength(contour,True) < 1000:
            newcountours.append(contour)
    # cv2.drawContours(img,contours,-1,(0,255,0),2)
    print(len(contours),len(newcountours))
    for a in newcountours:
        print(cv2.arcLength(a,True),cv2.contourArea(a))
        (x,y),radius = cv2.minEnclosingCircle(a)
        center = (int(x),int(y))
        radius = int(radius)
        #cv2.circle(img,center,radius,(0,255,0),2)
        x,y,w,h = cv2.boundingRect(a)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.imshow('frame',img)
        k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()