# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:39:02 2020

@author: utenti
"""

import numpy as np
import cv2

img = cv2.imread('res/chomsky.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('',image)

img1 = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('',img1)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()