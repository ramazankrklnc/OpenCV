# Probability Huffman Line Detection: Huffman Olasılıksal Çizgi Tespiti
# Görüntülerde binary görüntüye çevirme işlemi yapılarak
# görüntüdeki birbirinden farklı uzunluk ve açılardaki çizgilerin tespiti olasılıksal yaklaşım ile gerçekleştirilir.

import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow('canny_output', canny_output)
    return canny_output

src = cv.imread("OpenCV301/ImageFile/morph01.jpg")
cv.namedWindow('Input', cv.WINDOW_AUTOSIZE)
cv.imshow("Input", src)
cv.waitKey(0)

binary = canny_demo(src)
cv.imshow("Binary", binary)
cv.waitKey(0)

# cv.HoughLinesP ile doğru şekilde satırları bulun
linesP = cv.HoughLinesP(binary, 1, np.pi/180, 50, minLineLength=50, maxLineGap=10)

if linesP is not None:
    for i in range(len(linesP)):
        l = linesP[i][0]
        cv.line(src, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv.LINE_AA)

cv.imshow("Lines", src)
cv.waitKey(0)
cv.destroyAllWindows()






