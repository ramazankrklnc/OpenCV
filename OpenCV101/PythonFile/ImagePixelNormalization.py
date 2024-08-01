import cv2 as cv
import numpy as np

path = "OpenCV_Notes/ImageFile/"
src = cv.imread(path + "openCV.png")

print(src.shape)  # Resmimizin boyutuna eriştik

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY) # Gri renge çevirdik.
cv.imshow("gray", gray)
cv.waitKey(0)
print(gray.shape)   # Gri renkteki resmimizin boyutuna eriştik.

print(gray)  # Burada gray'in içeriğine baktık. Bütün sayısal değerleri integer. Bunu float'a çevirmemiz gerekiyor.

gray = np.float32(gray)  # Bunları ondalıklı yapma nedenimiz standartlaştırma işlemini gerçekleştirmek için lazım olacak.
print(gray)

# Min-Max Normalizasyon Yöntemi: Bu yöntem verilen iki değer arasında dönüştürme işlemi yapar.

# Standartlaştırmadan önceki hali;
min_value , max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

means, stdDev = cv.meanStdDev(gray)
print("mean: %.2f, stdDev: %.2f" % (means, stdDev))

# Sıfırlardan oluşan çıktı array'i;
dst = np.zeros(gray.shape, dtype=np.float32)

# 0 ile 1 arasında dönüştürme işlemini gerçekleştirme
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)

# Float'ı integer'a çevirme;
cv.imshow("NORM_MINMAX", dst)
cv.waitKey(0)

min_value , max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

means, stdDev = cv.meanStdDev(dst)
print("mean: %.2f, stdDev: %.2f" % (means, stdDev))

# NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(0)

# NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1, beta=0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(0)

# NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1, beta=0, norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000))
cv.waitKey(0)