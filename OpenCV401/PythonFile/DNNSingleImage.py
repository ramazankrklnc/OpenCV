import cv2 as cv
import numpy as np

modelBin = "OpenCV501/DNNFile/MobileNetSSD_deploy.caffemodel"
configText = "OpenCV501/DNNFile/MobileNetSSD_deploy.prototxt"

objName = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow",
           "diningtable", "dog", "horse", "motorbike", "person",
           "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

net = cv.dnn.readNet(modelBin, configText)

image = cv.imread("OpenCV501/ImageFile/dogs.jpg")
h = image.shape[0]
w = image.shape[1]

layerNames = net.getLayerNames()
lastLayerId = net.getLayerId(layerNames[-1])
lastLayer = net.getLayer(lastLayerId)

blob = cv.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False)
net.setInput(blob)
cvOut = net.forward()

for detection in cvOut[0, 0, :, :]:
    score = float(detection[2])
    objIndex = int(detection[1])
    if score > 0.5:
        left = detection[3] * w
        top = detection[4] * h
        right = detection[5] * w
        bottom = detection[6] * h
        cv.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness=2)
        cv.putText(image, "score:%.2f, %s" % (score, objName[objIndex]),
                   (int(left) - 10, int(top) - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8)

cv.imshow("mobilenet-ssd-demo", image)
cv.imwrite("result.png", image)
cv.waitKey(1)
