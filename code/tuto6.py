# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:03:42 2020

@author: utenti
"""

import cv2
import numpy as np

# B G R

img = cv2.imread('res/Kalluto.png')
    
colors = img[100,100]
print(colors)

blue = img[100,100,0]
print(blue)

print(img.item(100,100,0))
img.itemset((100,100,0),255)
print(img.item(100,100,0))

print(img.shape)
print(img.size)
print(img.dtype)

eye = img[400:700,700:900]

img[0:300,0:200] = eye


cv2.imshow('',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
#"""