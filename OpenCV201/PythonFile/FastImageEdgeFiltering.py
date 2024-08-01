# Edge Preserving Filter = Kenar Koruma Filtresi
# Bu filtre resim veya videolara uygulanır.

import cv2 as cv
import numpy as np

src = cv.imread("OpenCV301/ImageFile/test.jpeg")
cv.imshow("input", src)
cv.waitKey(0)

# Resmin boyut bilgilerini öğrenelim
h, w = src.shape[:2]

dst = cv.edgePreservingFilter(src, sigma_r=0.4, sigma_s=100, flags=cv.RECURS_FILTER)
# sigma s parametresi 0 ile 200 arasında değer alır. Ve resime uygulanacak olan blurluğu ifade eder.
# sigma r parametresi 0 ile 1 arasında değer alır. ve resmin genel hatları dışındaki kenarların ne kadar dikkate alınacağını belirler.

# İki resmi yan yana koyarak gözlemleyelim;
result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[:h, :w, :] = src
result[0:h, w:, :] = dst
cv.imshow("result", result)
cv.waitKey(0)