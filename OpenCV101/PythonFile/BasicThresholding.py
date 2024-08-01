import cv2 as cv
import numpy as np

path = "OpenCV_Notes/ImageFile/"
src = cv.imread(path + "work.jpg")

T = 127   # Threshold değerimiz

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)
    cv.waitKey(0)




