# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:18:53 2020

@author: utenti
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "C:/Users/utenti/Desktop/Desktop/OpenCV/"

img_rgb = cv2.imread(path+"res/mario_level.jpg")


img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread(path+"res/mario_template.jpg",0)

w,h = template.shape

#CHECK OTHER TEMPLATE MATCHING METHODS
result = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.7

loc = np.where(result >= threshold)

img2 = img_rgb.copy()
for point in zip(*loc[::-1]):
    cv2.rectangle(img2,point,(point[0]+h,point[1]+w),(0,0,255),2)
    
cv2.imshow('template',template)
cv2.imshow('result',img2)
cv2.imwrite(path+'res/mario_template_match.png',img2)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
#"""