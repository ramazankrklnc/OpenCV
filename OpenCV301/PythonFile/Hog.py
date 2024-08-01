# HOG (Histogram of Oriented Gradients) Pedestrian Detection

import cv2 as cv
import numpy as np

src = cv.imread("OpenCV401/ImageFile/pedestrian.jpg")

hog = cv.HOGDescriptor()

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.25)

for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('src', src)
cv.waitKey(0)