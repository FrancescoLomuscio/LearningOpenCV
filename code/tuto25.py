# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:33:51 2020

@author: utenti
"""

import cv2
import numpy as np

path = "C:/Users/utenti/Desktop/Desktop/OpenCV/"

img = cv2.imread(path+"res/building.jpg")

surf = cv2.SURF(400)

kp,des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

surf.hessianThreshold = 50000
kp2, des = surf.detectAndCompute(img,None)
img3 = cv2.drawKeypoints(img,kp2,None,(255,0,0),4)

cv2.imshow('img2',img2)

cv2.imshow('img3',img3)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

