import cv2 as cv
import numpy as np

path = "OpenCV_Notes/ImageFile/"

img1 = cv.imread(path + "rightSpiderman.jpg")
img2 = cv.imread(path + "leftSpiderman.jpg")

horizontal = np.hstack((img1, img2))
cv.imshow("spiderman", horizontal)
cv.waitKey(0)

# Oluşturulan yeni dosyayı kaydetme
cv.imwrite(path + "spiderman.jpg", horizontal)
cv.destroyAllWindows()

cv.destroyAllWindows()