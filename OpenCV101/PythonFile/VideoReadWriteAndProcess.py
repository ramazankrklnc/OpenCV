import cv2 as cv

capture = cv.VideoCapture(0)   # Dahili kamera ise 0 harici kamera ise 1
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

def process(image, opt=1):
    dst = None
    if opt == 0:
        dst = cv.bitwise_not(image)
    if opt == 1:
        dst = cv.GaussianBlur(image, (0, 0), 15)
    if opt == 2:
        dst = cv.Canny(image, 100, 200)
    return dst


index = 1
while True:
    ret, frame = capture.read()
    if ret is True:
        cv.imshow('video_input', frame)
        c = cv.waitKey(20)
        if c >= 19:
            index = c -19
        result = process(frame, index)
        cv.imshow('result', result)
        # print(s,,c)
        if c == 27:  # ESC
            break
    else:
        break

cv.waitKey(0)

