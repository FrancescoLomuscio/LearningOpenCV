# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:44:25 2020

@author: utenti
"""

import numpy as np
import cv2

capture = cv2.VideoCapture(0)
""" isOpened() controlla che la cattura sia sta inizializzata correttamente
altrimenti si usa il metodo open() per forzare l'apertura """
while(capture.isOpened()):
    """ ret e' True quando il frame viene letto correttamente """
    ret, frame = capture.read()
    if(ret):
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("grayscale camera", grayscale)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        
capture.release()
cv2.destroyAllWindows()

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("res/output.avi",fourcc,24,(640,480))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow("frame",frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else: 
        break

capture.release()
out.release()
cv2.destroyAllWindows()