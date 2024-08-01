import cv2 as cv
import numpy as np

cap = cv.VideoCapture("OpenCV301/VideoFile/Emre Fel - Sana El Pençe Durmam.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=500, detectShadows=False)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()
    cv.imshow('Input', frame)
    cv.imshow('Mask', fgmask)
    cv.imshow('Background', background)
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break