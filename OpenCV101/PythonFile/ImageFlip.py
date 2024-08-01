import cv2 as cv
import numpy as np

path = "OpenCV_Notes/ImageFile/"
src = cv.imread(path + "openCV.png")

# X eksenine göre çevirme
dst1 = cv.flip(src, 0)
cv.imshow("X-Flip", dst1)
cv.waitKey(0)

# Y eksenine göre çevirme
dst2 = cv.flip(src, 1)
cv.imshow("Y-Flip", dst2)
cv.waitKey(1)

# Hem X hem Y eksenine göre çevirme işlemi
dst3 = cv.flip(src, -1)
cv.imshow("Y-Flip", dst3)
cv.waitKey(1)


