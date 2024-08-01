import cv2 as cv

path = "OpenCV_Notes/ImageFile/"
# Yukarıda oluşturulan path aynı dizin altında olan tüm jpg uzantılı dosyaları
# aşağıdaki gibi tek tek okuyabilelim diye oluşturuldu.

img = cv.imread(path + "cat.jpg")

type(img)

# nameWindow
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

# imshow
cv.imshow("opencv_test", img)
cv.waitKey(0)

cv.destroyAllWindows()   # Açıkta olan tüm pencereleri kapatmış olduk