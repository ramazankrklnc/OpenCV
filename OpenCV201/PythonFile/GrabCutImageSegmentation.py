import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/m1.jpg")

src = cv.resize(src, (0,0), fx=0.5, fy=0.5)
cv.imshow("Original", src)
cv.waitKey(0)

r = cv.selectROI("Input", src, False)

roi = src[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]
img = src.copy()

cv.rectangle(img, (int(r[0]), int(r[1])), (int(r[0] + r[2]), int(r[1] + r[3])), (0, 255, 0), 2)

mask = np.zeros(src.shape[:2], dtype=np.uint8)

# Seçilen kısımın ayrıştırılma işlemi
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

bdgmodel = np.zeros((1,65), np.float64)
fdgmodel = np.zeros((1,65), np.float64)

cv.grabCut(src, mask, rect, bdgmodel, fdgmodel, 11, mode=cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

result = cv.bitwise_and(src, src, mask=mask2)

cv.imshow("Ilk Hali", roi)
cv.imshow("Son Hali", result)
cv.waitKey(0)