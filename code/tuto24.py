# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:20:48 2020

@author: utenti
"""

import cv2
import numpy as np


path = "C:/Users/utenti/Desktop/Desktop/OpenCV/"

img = cv2.imread(path+'res/building.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()