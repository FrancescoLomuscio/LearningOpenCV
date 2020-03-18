# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:16:59 2020

@author: utenti
"""

import cv2
import numpy as np

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

blue = np.uint8([[[255,0,0 ]]])
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)

red = np.uint8([[[0,0,255]]])
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

print(hsv_blue)
print(hsv_green)
print(hsv_red)

capture = cv2.VideoCapture(0)

while(capture.isOpened()):
    ret, frame = capture.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])
    
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    
    mask_b = cv2.inRange(hsv,lower_blue,upper_blue)
    
    mask_g = cv2.inRange(hsv,lower_green,upper_green)
    
    mask_r = cv2.inRange(hsv,lower_red,upper_red)
    
    result = cv2.bitwise_and(frame,frame,mask = mask_b)
    
    result2 = cv2.bitwise_and(frame,frame,mask = mask_g)
    
    result3 = cv2.bitwise_and(frame,frame,mask = mask_r)
    
    res = cv2.add(result,result2)
    res = cv2.add(res,result3)
    
    cv2.imshow('frame',frame)
    cv2.imshow('maskb',mask_b)
    cv2.imshow('maskg',mask_g)
    cv2.imshow('maskr',mask_r)
    cv2.imshow('resb',result)
    cv2.imshow('resg',result2)
    cv2.imshow('resr',result3)
    cv2.imshow('res',res)
    
    
    
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