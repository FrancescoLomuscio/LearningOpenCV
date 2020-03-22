# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:24:29 2020

@author: utenti
"""

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("res/Chomsky.jpg")

cv2.namedWindow('example')
cv2.createTrackbar('Min','example',0,1000,nothing)
cv2.createTrackbar('Max','example',0,1000,nothing)
cv2.imshow('example',img)
while 1:
    k = cv2.waitKey(1)
    if k == 27:
        break
        
    min = cv2.getTrackbarPos('Min','example')
    max = cv2.getTrackbarPos('Max','example')
    
    edges = cv2.Canny(img,min,max)
    cv2.imshow('example',edges)

cv2.destroyAllWindows()