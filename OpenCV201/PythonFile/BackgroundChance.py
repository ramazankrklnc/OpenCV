import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/m1.jpg")
src = cv.resize(src, (0,0), fx=0.5, fy=0.5)
r = cv.selectROI("Input", src, False)

roi = src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
img = src.copy()

cv.rectangle(img, (int(r[0]), int(r[1])), (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])), (255, 0, 0), 2)
mask = np.zeros(src.shape[:2], dtype=np.uint8)
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

bdgmodel = np.zeros((1,65), np.float64)
fdgmodel = np.zeros((1,65), np.float64)

cv.grabCut(src, mask, rect, bdgmodel, fdgmodel, 11, mode=cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

# Arka planı değiştirme
background = cv.imread("OpenCV301/ImageFile/flower.jpg")

h, w, ch = src.shape
background = cv.resize(background, (w, h))
mask = np.zeros(src.shape[:2], dtype=np.uint8)
bdgmodel = np.zeros((1,65), np.float64)
fdgmodel = np.zeros((1,65), np.float64)

# grabCut arka planı değiştirmemizi sağlayan fonksiyonumuzdur.
cv.grabCut(src, mask, rect, bdgmodel, fdgmodel, 5, mode=cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')


se = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))

# Genişletme İşlemi
cv.dilate(mask2, se, mask2)

# Birleştirme işleminde kenarların yumuşak geçişini sağlamak için;
mask2 = cv.GaussianBlur(mask2, (5, 5), 0)

# Çıkış Matrisi;
background = cv.GaussianBlur(background, (0, 0), 15)
mask2 = mask2 / 255.0
a = mask2[..., None]
result = a * (src.astype(np.float32)) + (1 - a) * (background.astype(np.float32))

cv.imshow("Result", result.astype(np.uint8))
cv.waitKey(0)

