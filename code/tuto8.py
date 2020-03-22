# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:58:27 2020

@author: utenti
"""

import cv2
import numpy as np

print(cv2.useOptimized())
img = cv2.imread("res/Kalluto.png")
t1 = cv2.getTickCount()

for i in range(5,49,2):
    img = cv2.medianBlur(img,i)
t2 = cv2.getTickCount()

time = (t2 - t1) / cv2.getTickFrequency()

print(time)

cv2.setUseOptimized(False)
print(cv2.useOptimized())
img = cv2.imread("res/Kalluto.png")
t1 = cv2.getTickCount()

for i in range(5,49,2):
    img = cv2.medianBlur(img,i)
t2 = cv2.getTickCount()

time = (t2 - t1) / cv2.getTickFrequency()

print(time)