import cv2 as cv
import numpy as np

src = cv.imread("OpenCV401/ImageFile/openCV.png")

# Tuz biber gürültüsünü ekleme
def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(low=0, high=h, size=nums, dtype=np.int32)
    cols = np.random.randint(low=0, high=w, size=nums, dtype=np.int32)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)  # Tek sayılara beyaz gürültü ekleme
        else:
            image[rows[i], cols[i]] = (0, 0, 0)        # Çift sayılara siyah gürültü ekleme
    return image

h, w = src.shape[:2]

copy = np.copy(src)

copy = add_salt_pepper_noise(copy)

# Görüntünün ilk hali ile gürültü eklenmiş halini gözlemleyelim;
result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = copy

cv.imshow("Output", result)
cv.waitKey(0)