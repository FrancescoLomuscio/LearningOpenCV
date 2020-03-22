# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:40:15 2020

@author: utenti
"""

import cv2
import numpy as np

img = cv2.imread("res/Joe.jpg",0)
rows,cols = img.shape

cv2.imshow("esempio",img)

res = cv2.resize(img,None,fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("resize",res)

M = np.float32([[1,0,50],[0,1,25]])
dts = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("dts",dts)

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
rot = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("rot",rot)

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
rot2 = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("rot2",rot2)

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('',dst)

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

cv2.imshow("perp",dst)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
#"""