import cv2 as cv
import numpy as np

path = "OpenCV_Notes/ImageFile/"

src = cv.imread(path + "openCV.png", cv.IMREAD_GRAYSCALE)

# minMaxLoc
min_value , max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))   # Buradaki print min ve maxın değerlerini return etti.
print("min_loc:", min_loc, ",", " max_loc:", max_loc)   # Burada ise yukarıda bulununan max ve minin lokasyonları return etti.

# meanStdDev = Ortalama ve Standart Sapma Değerleri
means, stdDev = cv.meanStdDev(src)
print("mean: %.2f, stdDev: %.2f" % (means, stdDev))

src[np.where(src < means)] = 0
src[np.where(src > means)] = 255

cv.imshow("binary", src)
cv.waitKey(0)

