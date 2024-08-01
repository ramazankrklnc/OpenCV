import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/keanu.jpeg")
cv.imshow("keanu", src)
cv.waitKey(0)

edge = cv.Canny(src, 100, 300)
# içine aldığı iki argümanı linklemek için kullanıyor.
cv.imshow("mask image", edge)
cv.waitKey(0)