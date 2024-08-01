# Geometrik Dönüşümler: Bir pikselin eski konumundan yeni konumuna taşınması(affine) haritalanması işlemidir.
import cv2
import cv2 as cv
import numpy as np

# Shifting = Kaydırma İşlemi
img = cv.imread("OpenCV301/ImageFile/Cat.jpg")

rows = img.shape[0]
cols = img.shape[1]
print(rows,cols)

M = np.float32([[1, 0, 300], [0, 1, 90]])
shifted = cv.warpAffine(img, M, (cols, rows))

cv.imshow("Original", img)
cv.waitKey(1)

cv.imshow("Shifted", shifted)
cv.waitKey(1)

# Rotation = Döndürme İşlemi
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow("Rotation", dst)
cv.waitKey(0)

# Scaling = Ölçeklendirme
res = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", res)
cv.waitKey(0)

res = cv.resize(img, None, fx=1.2, fy=1.2, interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", res)
cv.waitKey(0)
