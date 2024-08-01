# BACKGROUND SUBTRACTION AND ROI EXTRACTION OF THE FOREGROUND

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("OpenCV301/VideoFile/Emre Fel - Sana El Pençe Durmam.avi")

fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=100, detectShadows=False)

def process(image):
    mask = fgbg.apply(image)
    lines = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 5), (-1, -1))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, lines)
    cv.imshow('mask', mask)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv.minAreaRect(contours[c])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image

# Yukarıdaki döngüyü while işlemi True olduğu sürece döndür diyebiliriz.

while True:
    ret, frame = cap.read()
    cv.imshow('Input', frame)
    result = process(frame)
    cv.imshow('Result', result)
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break


cv.destroyAllWindows()