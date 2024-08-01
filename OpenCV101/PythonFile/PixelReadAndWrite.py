import cv2 as cv

path = "OpenCV_Notes/ImageFile/"
img = cv.imread(path + "openCV.png")
cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)
cv.waitKey(0)

h, w, ch = img.shape
print("h, w, ch", h, w, ch)

# Amacımız openCV.png görselindeki beyaz olan kısımları siyah yapmak.
for row in range(h):
    for col in range(w):
        b, g, r = img[row][col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row][col] = (b, g, r)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
