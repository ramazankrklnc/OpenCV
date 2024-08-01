import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def customHist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype = np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1
    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color = "r", alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

src = cv.imread("OpenCV301/ImageFile/lab.jpg")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("Input", gray)
cv.waitKey(1)
customHist(gray)


# Histogram eşitleme
dst = cv.equalizeHist(gray)
cv.imshow("Equalized", dst)
cv.waitKey(1)

# Yeni oluşturulan görselin histogram grafiği
customHist(dst)