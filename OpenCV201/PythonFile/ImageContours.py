# Görüntünün sahip olduğu tüm noktaları birleştiren kapalı bir eğri oluşturularak kontur oluşturulur.
# Kontur Algılama: Şekil algılama ve analizi ve nesne algılama için kullanılabilen faydalı bir tekniktir.

import cv2 as cv
import numpy as np

def threshold_demo(image):
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary',binary)
    return binary

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image,t,t*2)
    cv.imshow('canny_output',canny_output)
    return canny_output

src = cv.imread("OpenCV301/ImageFile/lena.jpeg")
cv.namedWindow("Input", cv.WINDOW_AUTOSIZE)
cv.imshow("Input", src)
cv.waitKey(0)

binary = threshold_demo(src)
canny = canny_demo(src)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    cv.drawContours(src, contours, c, (0,0,255), 2, 8)

cv.imshow("ContoursDemo", src)
cv.waitKey(0)