# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:32:24 2020

@author: utenti
"""

import cv2
import numpy as np

img = cv2.imread("res/logo.png")

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
mfilter = cv2.medianBlur(img,5)

cv2.imshow('original',img)
cv2.imshow('kernel',dst)
cv2.imshow('blur',blur)
cv2.imshow('gblur',gblur)
cv2.imshow('mblur',mfilter)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()