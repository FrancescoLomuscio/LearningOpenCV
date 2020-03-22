# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:39:38 2020

@author: utenti
"""

import cv2 
import numpy as np

def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('example')

cv2.createTrackbar('R','example',0,255,nothing)
cv2.createTrackbar('G','example',0,255,nothing)
cv2.createTrackbar('B','example',0,255,nothing)

switch = '0: OFF \n1: ON'
cv2.createTrackbar(switch,'example',0,1,nothing)

while 1:
    cv2.imshow('example',img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
    r = cv2.getTrackbarPos('R','example')
    g = cv2.getTrackbarPos('G','example')
    b = cv2.getTrackbarPos('B','example')
    s = cv2.getTrackbarPos(switch,'example')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        
cv2.destroyAllWindows()