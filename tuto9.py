# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:16:59 2020

@author: utenti
"""

import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(capture.isOpened()):
    ret, frame = capture.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    
    result = cv2.bitwise_and(frame,frame,mask = mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',result)
    
    k = cv2.waitKey(5)
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()




"""
PER TROVARE VALORI DA TRACKARE CONVERTI IL COLORE CHE VUOI IN HSV E IL RANGE 
DA TROVARE IN HSV E' [H-10,100,100],[H+10,255,255]
>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]
"""