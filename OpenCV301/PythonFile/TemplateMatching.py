import cv2 as cv
import numpy as np

path = "OpenCV401/ImageFile/"


def templateDemo():
    src = cv.imread(path + "openCV.png")
    tpl = cv.imread(path + "openCV01.jpg")

    cv.imshow("Input", src)
    cv.imshow("Template", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(tpl, src, cv.TM_CCORR_NORMED)
    cv.imshow("Result", result)

    # cv.imwrite(path + "/result.png", np.unit8(result*255))
    t = 0.98  # threshold değerimiz kendimiz değerini belirledik. Ne kadar benzerlik oluşacağına karar veriyoruz.
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)

    cv.imshow("First Demo", src)


templateDemo()
cv.waitKey(0)
