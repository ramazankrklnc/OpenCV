# Otomatik görüntü eşikleme için kullanılan bir yöntemdir.
# Giriş olarak verilen görüntüyü ikili(binary - siyah, beyaz) görüntüye çevirir.

import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/lena.jpeg")
cv.namedWindow("Original", cv.WINDOW_AUTOSIZE)
cv.imshow("Original", src)
cv.waitKey(0)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

h, w = src.shape[:2]

cv.imshow("Binary", binary)
cv.waitKey(0)