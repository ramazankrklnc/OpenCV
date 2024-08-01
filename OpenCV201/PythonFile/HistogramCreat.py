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

def imageHist(image):
    cv.imshow("Input", image)
    color = ("blue", "green", "red")
    for i, col in enumerate(color):
        hist = cv.calcHist(image, [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread("OpenCV301/ImageFile/lab.jpg")
cv.namedWindow("Input", cv.WINDOW_AUTOSIZE)
cv.imshow("Input", src)
cv.waitKey(0)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
customHist(gray)
imageHist(src)    # Bu kod rgb renklerin dağılımını göstermeye yarıyor.
