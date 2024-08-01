import cv2 as cv

#HSV = Renklerin özü ve doygunluğu

# RGB Formundaki görselimiz;
img = cv.imread("OpenCV301/ImageFile/openCV.png")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(0)

# RGB'den GRAY'e çevirme;
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)

# RGB'den HSV'ye çevirme;
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey()


