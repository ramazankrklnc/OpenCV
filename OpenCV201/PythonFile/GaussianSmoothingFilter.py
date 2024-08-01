# BilateralFilter = Resmin kenarlarını koruyarak görüntüyü yumuşatmış oluyor.

import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/test.jpeg")
cv.namedWindow("Input", cv.WINDOW_AUTOSIZE)
cv.imshow("Input", src)
cv.waitKey(0)

# Resmin boyut bilgileri
h, w = src.shape[:2]

# Dönüştürme İşlemi
dst = cv.bilateralFilter(src, 0, 100, 20)

# Sonuçlar
result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[:h, :w, :] = src   # İlk hali
result[0:h, w:, :] = dst   # Dönüştürülmüş hali

cv.imshow("Output", result)
cv.waitKey(0)
