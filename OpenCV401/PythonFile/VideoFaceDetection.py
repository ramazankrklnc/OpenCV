import cv2 as cv
import numpy as np


modelBin = "OpenCV501/DNNFile/res10_300x300_ssd_iter_140000.caffemodel"
configText = "OpenCV501/DNNFile/deploy.prototxt"

net = cv.dnn.readNetFromCaffe(modelBin, configText)

net = cv.dnn.readNetFromCaffe(config_text, model_bin)

net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

cap = cv.VideoCapture(0)
while True:
    ret, image = cap.read()
    image = cv.flip(image, 1)
    if ret is False:
        break

    h, w = image.shape[:2]
    blobImage = cv.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0), False, False)
    net.setInput(blobImage)
    cvOut = net.forward()

    t, _ = net.getPerfProfile()
    fps = 1000 / (t * 1000.0 / cv.getTickFrequency())
    label = "cost time: %.2f ms" % fps
    cv.putText(image, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    for detection in cvOut[0, 0, :, :]:
        score = float(detection[2])
        # objIndex = int(detection[1])
        if score > 0.5:
            left = detection[3] * w
            top = detection[4] * h
            right = detection[5] * w
            bottom = detection[6] * h

            cv.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness=2)
            cv.putText(image, "score:%.2f" % score, (int(left), int(top)), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv.imshow('Video', image)
    c = cv.waitKey(2)
    if c == 27:
        break
cv.waitKey(0)


