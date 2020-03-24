# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:46:15 2020

@author: utenti
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
path = "C:/Users/utenti/Desktop/Desktop/OpenCV/"
img = cv2.imread(path+'res/Kalluto.png')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (500,500,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imshow("img",img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()