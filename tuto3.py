# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:46:30 2020

@author: utenti
"""

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)


img = cv2.line(img,(0,0),(511,511),(255,0,0),10)

img = cv2.rectangle(img,(300,0),(500,100),(0,255,0),3)

img = cv2.circle(img,(447,63), 50, (0,0,255), -1)

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("black image", img)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.destroyAllWindows()
