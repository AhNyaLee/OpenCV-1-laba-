import cv2
import numpy as np
cap=cv2.VideoCapture(r'video5444892193334510796.mp4')
while True:
    ret, frame =cap.read()
    if not(ret):
        break
    cv2.imshow('frame',frame)
