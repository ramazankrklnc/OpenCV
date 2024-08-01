import cv2 as cv
import numpy as np

src = cv.imread("OpenCV401/ImageFile/openCV.png")

# Görüntünün bir araya gelmesini istediğimiz iki matrisi oluşturma;
sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)

# Keskinleştirme için kullanılacak method;
sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op)

# Dönüştürme Fonksiyonu;
# Bu fonksiyon işaretleme, ölçekleme, mutlak değer alma ve işaretsiz 8 bitlik türe dönüştürme işlemini gerçekleştirir.
sharpen_image = cv.convertScaleAbs(sharpen_image)

cv.imshow("Sharpen Image", sharpen_image)
cv.waitKey(0)

