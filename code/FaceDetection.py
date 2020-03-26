# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:26:16 2020

@author: utenti
"""

import numpy as np
import cv2

def draw_face(img, classifier, subclassifiers, text, color):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elements = classifier.detectMultiScale(gray)
    for (x,y,w,h) in elements:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
        
        roi_color = img[y:y+h,x:x+w]
        texts = ["Eye","Mouth","Nose"]
        subcolor = (0,255,0)
        
        draw_elements(roi_color,subclassifiers,texts,subcolor)
        
def draw_elements(img,classifiers,texts,subcolor):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for classifier,text in zip(classifiers,texts):
        if text == "Eye":
            elements = classifier.detectMultiScale(gray,1.1,14)
        elif text == "Mouth":
            elements = classifier.detectMultiScale(gray,1.2,20)
        elif text == "Nose":
            elements = classifier.detectMultiScale(gray,1.5,4)
        for (x,y,w,h) in elements:
            cv2.rectangle(img,(x,y),(x+w,y+h),subcolor,2)
            cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,subcolor,1,cv2.LINE_AA)
        
path = "../XML/"
face_cascade = cv2.CascadeClassifier(path+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(path+'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(path+'haarcascade_smile.xml')
nose_cascade = cv2.CascadeClassifier(path+'Nariz.xml')

capture = cv2.VideoCapture(0)
""" isOpened() controlla che la cattura sia sta inizializzata correttamente
altrimenti si usa il metodo open() per forzare l'apertura """
while(capture.isOpened()):
    """ ret e' True quando il frame viene letto correttamente """
    ret, frame = capture.read()
    if(ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = frame
        
        draw_face(img,face_cascade,[eye_cascade,smile_cascade,nose_cascade],"Face",(255,0,0))
        
        """eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)"""
        
        cv2.imshow('img',img)
        k = cv2.waitKey(1)
        if k == 27:
            break
        
capture.release()
cv2.destroyAllWindows()