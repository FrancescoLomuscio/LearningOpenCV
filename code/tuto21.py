# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:20:59 2020

@author: utenti
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt


#CARIMENTO IMMAGINE
path = "C:/Users/utenti/Desktop/Desktop/OpenCV/"
img = cv2.imread(path+"res/water_coins.jpg")
cv2.imshow('img', img)

#THRESHOLD PER TROVARE MAPPA BINARIA CONTENENTE CONTORNO MONETE
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('mask', thresh)

#PULIZIA DEL RUMORE
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
cv2.imshow('opening',opening)

#CREAZIONE BACKGROUND
sure_bg = cv2.dilate(opening,kernel,iterations=3)
cv2.imshow('background',sure_bg)

#CREAZIONE FOREGROUND
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv2.imshow('fg',sure_fg)

#CREAZIONE SURE FOREGROUND
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow('unkwnown',unknown)

#DISEGNO CONTORNI
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
cv2.imshow('result',img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()