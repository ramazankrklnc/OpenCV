import cv2 as cv
import numpy as np

path = "OpenCV_Notes/ImageFile/"
img = cv.imread(path + "cat.jpg")
cv.namedWindow("imageCreat", cv.WINDOW_AUTOSIZE)
cv.imshow("imageCreat", img)
cv.waitKey(0)

# Resmin kopyasını alıp üzerinde işlemleri gerçekleştiricez.
m1 = np.copy(img)
m2 = img    # Burda ise orijinal resim

type(img)

img[100:200, 200:300, :] = 255    # Bu resim içinde seçtiğimiz kısımın beyaz olmasını sağlıyor. 0 olsa siyah olacaktı.
img[100:200, 200:300, :] = 0      # Buradaki gibi
# Alttaki iki satırda bize ekranda göstermemizi sağladı.
cv.imshow("m2", m2)
cv.waitKey(0)


# Resimle aynı boyutta 0 oluşturma yani tamamı siyah olan bir resim oluşturmuş olucaz.
m3 = np.zeros(img.shape, img.dtype)
cv.imshow("m3", m3)
cv.waitKey(1)

# Farklı boyutta 0 oluşturma
m4 = np.zeros([512,512], np.uint8)
cv.imshow("m4", m4)
cv.waitKey(1)

# Gri renkte görseli oluşturma
m5 = np.zeros([512,512], np.uint8)
m5[ : , :] = 127
cv.imshow("m5", m5)
cv.waitKey(0)


# Kendimiz bir şekil çizersek;
img = np.ones((550, 770, 3))
black = (0 , 0 , 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Dikdörtgeni çizme;
cv.rectangle(img, (480, 250), (100, 450), black, 8)
cv.rectangle(img, (580, 150), (200, 350), black, 8)

# Dikdörtgen için çizgileri ayarlama;
cv.line(img, (100, 450), (200, 350), black, 8)
cv.line(img, (480, 250), (580, 150), black, 8)
cv.line(img, (100, 250), (200, 150), black, 8)
cv.line(img, (480, 450), (580, 350), black, 8)

# Resmin üzerine yazı yazmak istersek ve eklenecek yeri ayarlarsak;
start_point = (150, 100)
font_thickness = 1
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX

cv.putText(img, "www.kendim3Ddikdortgencizdim.com", start_point, font, font_size, black, font_thickness)
cv.imshow("dikdortgen", img)
cv.waitKey(0)
