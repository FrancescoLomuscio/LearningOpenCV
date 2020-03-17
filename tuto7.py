# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:13:33 2020

@author: utenti
"""

import cv2
import numpy as np

img1 = cv2.imread("res/Kalluto.png")

img2 = cv2.imread("res/logo.png")

img3 = img2 - 100

rows,cols,chans = img2.shape

roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('',img1)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()    