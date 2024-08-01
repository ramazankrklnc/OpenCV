# Kenar algılama işlemi renk geçişlerinin fark edilmesi olayıdır.
# Sobel Filtresi resimlerden türevleri yakalamamıza yardımcı olur.
import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/openCV.png")
h, w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

# Sobel filtresinde Dikey Çekirdeğin Kullanılması: X yönünde geliştirilmiş kenarları olan bir sobel görüntüsü elde etmek demektir.
# y_grad ise yatay eksende bir sobel görüntüsü elde edicez demek.

# Yakalanılan türevleri dönüştürme; Ölçeklendirme
x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

cv.imshow("x_grad", x_grad)
cv.waitKey(1)

cv.imshow("y_grad", y_grad)
cv.waitKey(1)

# Birleştirme
add = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
add = cv.convertScaleAbs(add)
cv.imshow("Gradient", add)
cv.waitKey(0)



