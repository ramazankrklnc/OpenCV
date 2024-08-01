# KLT Tabanlı Optik Akış

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("OpenCV301/VideoFile/Emre Fel - Sana El Pençe Durmam.avi")
ret, frame1 = cap.read()

prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

hsv = np.zeros_like(frame1, dtype=np.uint8)
hsv[..., 1] = 255

def dense_optical_flow(hsv, prvs):
    while 1:
        ret, frame2 = cap.read()
        nextt = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
        flow = cv.calcOpticalFlowFarneback(prvs, nextt, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang= cv.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
        bgr = cv.cvtColor(hsv, cv.COLOR_BGR2RGB)
        cv.imshow('frame2', bgr)
        cv.imshow('frame1', frame2)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
        prvs = nextt

dense_optical_flow(hsv, prvs)
