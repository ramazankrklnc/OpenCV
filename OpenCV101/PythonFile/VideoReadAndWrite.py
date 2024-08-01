import cv2 as cv
import numpy as np

capture = cv.VideoCapture("OpenCV_Notes/VideoFile/Emre Fel - Sana El Pençe Durmam.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

# Yukarıda videoyu okuduk. Şimdi yazdırırsak;

out = cv.VideoWriter("OpenCV_Notes/VideoFile/Emre Fel - Sana El Pençe Durmam.avi",
                     cv.VideoWriter_fourcc("D", "I", "V", "X"), 15,
                     (np.int32(width), np.int32(height)), True)

while True:
    # kameradan görüntü al
    ret, frame = capture.read()

    # Görüntü başarıyla alındı mı kontrol et
    if ret is True:
        # Okunan görüntüyü ekranda göster
        cv.imshow('video_input', frame)
        out.write(frame)
        # 50 sn sonra çık
        c = cv.waitKey(50)
        if c == 27:  # ESC
            break
    else:
        break

capture.release()   # Pencereyi kapat
out.release()       # Geçici ön belleğini temizle
