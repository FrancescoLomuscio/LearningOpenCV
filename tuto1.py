# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:18:39 2020

@author: utenti
"""


""" LEZIONE 1 """
import numpy as np
import cv2

img = cv2.imread("Kalluto.png",0)

cv2.imshow("Kalluto",img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.destroyAllWindows()
    
    cv2.imwrite("KallutoGrayScale.png",img)
""" FINE LEZIONE 1 """