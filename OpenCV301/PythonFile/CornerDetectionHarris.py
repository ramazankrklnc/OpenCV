import cv2 as cv
import numpy as np

src = cv.imread("OpenCV401/ImageFile/chessboard.jpg")

def harris(image):
    blockSize = 2   # Köşe tespiti için düşünülen komşuluk boyutu
    apertureSize = 3   # Sobel yöntemi için diafram parametresi
    k = 0.04           # Harrisin serbestlik parametresi

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, 0, 255, norm_type=cv.NORM_MINMAX)

    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), thickness=2)

    return image

result = harris(src)
cv.imshow("result", result)
cv.waitKey(0)
