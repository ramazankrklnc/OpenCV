import cv2 as cv
import numpy as np

path = "OpenCV501/ImageFile/"
src = cv.imread(path + "QRCode.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

QRCoder = cv.QRCodeDetector()  # Bu fonksiyon saptamak istenilen görüntüyü alır.

codeinfo, points, straight_qrcode = QRCoder.detectAndDecode(gray)

print(points)

result = np.copy(src)

# Resme kontur çizelim
cv.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)
# thickness = kalınlık
print("QRCode information is: \n%s" % codeinfo)  # Bu kod ile QR kodun içerisinde saklı olan metini açtık.

# Resmin konturlu halini göstermek istersek;
cv.imshow("QRCode", result)
cv.waitKey(0)