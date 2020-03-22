# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:57:41 2020

@author: utenti
"""

import cv2
import numpy as np

img = cv2.imread("res/sudoku.jpg",0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)
sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)

cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('sobel',sobel)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()