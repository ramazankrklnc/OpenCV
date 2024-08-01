# ROI(Region of Interest) = İlgilenilen Alan resimde istediğimiz kısım üzerinde çalışmamızı sağlar.

import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/Cat.jpg")

h,w = src.shape[:2]

img = src.copy()

roi = img[80:650, 400:600, :]

roi.shape[:2]

cv.imshow("ROI",roi)
cv.waitKey(0)

# Roi bölgemizi ana resmimize eklersek;
img[0:570, 0:200, :] = roi
cv.imshow("ROI",img)
cv.waitKey(0)

# roi bölgesini küçültmek istersek;
res = cv.resize(roi,None,fx=0.7,fy=0.7, interpolation=cv.INTER_CUBIC)
cv.imshow("res",res)
cv.waitKey(0)

# Küçültülen resmin boyutlarına bakıp onu da normal resmimizin üstüne koyalım;
res.shape[:2]

img[0:399, 0:140, :] = res
cv.imshow("ROI", img)
cv.waitKey(0)
# yukarıdaki kod da iki tane görsel ana görsel üstüneydi.
# Şimdi ise en son oluşturlan resmi sadece ana resme koyarsak;

src[0:399, 0:140, :] = res
cv.imshow("ROI", src)
cv.waitKey(0)


