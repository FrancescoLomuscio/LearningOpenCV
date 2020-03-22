import cv2
import numpy as np,sys

A = cv2.imread('res/apple.jpg')
lower = cv2.pyrDown(A)

cv2.imshow('',lower)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()