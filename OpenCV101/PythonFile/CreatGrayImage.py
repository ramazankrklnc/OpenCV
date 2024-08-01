import cv2 as cv

path = "OpenCV_Notes/ImageFile/"
img = cv.imread(path + "cat.jpg")

cv.namedWindow("colored", cv.WINDOW_AUTOSIZE)
cv.imshow("colored", img)
cv.waitKey(0)

# Resmin Formatını değiştirmek için kullanacağımız kod: cvtColor

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(0)

# Gri formattaki resmi kaydetme
cv.imwrite(path + "gray_opencv.jpg", gray)
cv.destroyAllWindows()



# Yukarıdaki işlemleri uzun uzun yazmadan resimleri griye direk çevirme işlemi
img = cv.imread(path + "cat.jpg", cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
cv.imshow("gray", img)
cv.waitKey(0)
