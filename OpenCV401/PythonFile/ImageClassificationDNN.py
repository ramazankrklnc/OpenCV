# DNN (Deep Neural Network) Görüntü Sınıflandırma
# GOOGLENET Modeline Ait Katmanların Bilgilerini Okuma
"""
import cv2 as cv
import numpy as np

path = "OpenCV501/ImageFile/"

binModel = "OpenCV501/DNNFile/bvlc_googlenet.caffemodel"
proTxt = "OpenCV501/DNNFile/deploy.prototxt"

net = cv.dnn.readNet(proTxt, binModel)

layerNames = net.getLayerNames()

for name in layerNames:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id: %d, type: %s, name: %s" % (id, layer.type, name))

# GOOGLENET Modeli ile Görüntü  Sınıflandırma
with open("OpenCV501/DNNFile/imagenet1000_clsidx_to_labels.txt", "rt") as f:
    classes = f.read().split("\n")

net = cv.dnn.readNetFromCaffe(proTxt, binModel)

# Nesne Tespiti yapılacak resimlerimiz
image1 = cv.imread(path + "guineaPig.jpg")
image2 = cv.imread(path + "dog.jpg")

blob = cv.dnn.blobFromImage(image1, 1.0, (224, 224), (104, 117, 123), swapRB=False, crop=False)

result = np.copy(image1)

net.setInput(blob)

out = net.forward()

out = out.flatten()
# Flatten iki olan boyutu tek boyuta düşürdü.

classID = np.argmax(out)

# Output içersinden ID'yi çağıralım;
confidence = out[classID]

# Bu kısımda modelin performansı ile ilgili bir raporlama yaptık.
t, _ = net.getPerfProfile()
label = "cost time: %.2f ms" % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

# Bu kısımda ise label'in ne olduğu ile ilgili bilgiyi çıkarma işlemini gerçekleştirdik.
label = "%s: %.4f" % (classes[classID] if classes else "Class #%d" % classID, confidence)

# İlgili resmin üstüne çıktıyı eklersek;
cv.putText(result, label, (0, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

show_img = np.hstack((image1, result))
cv.imshow("Result", show_img)
cv.waitKey(0)

# Fotoğraf çıktısı sığmadığı için burada boyutuna baktım.
dst = image1.shape[:2]
"""

# Aşağıya yazdığım kod sadece görselin pencereye sığması için ChatGPT tarafından yazıdırıldı.
import cv2 as cv
import numpy as np

path = "OpenCV501/ImageFile/"

binModel = "OpenCV501/DNNFile/bvlc_googlenet.caffemodel"
proTxt = "OpenCV501/DNNFile/deploy.prototxt"

net = cv.dnn.readNet(proTxt, binModel)

layerNames = net.getLayerNames()

for name in layerNames:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id: %d, type: %s, name: %s" % (id, layer.type, name))

# GOOGLENET Modeli ile Görüntü Sınıflandırma
with open("OpenCV501/DNNFile/imagenet1000_clsidx_to_labels.txt", "rt") as f:
    classes = f.read().split("\n")

net = cv.dnn.readNetFromCaffe(proTxt, binModel)

# Nesne Tespiti yapılacak resimlerimiz
image1 = cv.imread(path + "guineaPig.jpg")
image2 = cv.imread(path + "dog.jpg")

# Görselleri yeniden boyutlandır (745x1118).
desired_width = 745
desired_height = 1118
image1_resized = cv.resize(image1, (desired_width, desired_height))
image2_resized = cv.resize(image2, (desired_width, desired_height))

blob = cv.dnn.blobFromImage(image1_resized, 1.0, (224, 224), (104, 117, 123), swapRB=False, crop=False)

result = np.copy(image1_resized)

net.setInput(blob)

out = net.forward()

out = out.flatten()
# Flatten iki olan boyutu tek boyuta düşürdü.

classID = np.argmax(out)

# Output içersinden ID'yi çağıralım;
confidence = out[classID]

# Bu kısımda modelin performansı ile ilgili bir raporlama yaptık.
t, _ = net.getPerfProfile()
label = "cost time: %.2f ms" % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

# Bu kısımda ise label'in ne olduğu ile ilgili bilgiyi çıkarma işlemini gerçekleştirdik.
label = "%s: %.4f" % (classes[classID] if classes else "Class #%d" % classID, confidence)

# İlgili resmin üstüne çıktıyı eklersek;
cv.putText(result, label, (0, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Görselleri yatay olarak birleştir.
show_img = np.hstack((image1_resized, result))

# Pencereyi manuel olarak boyutlandır.
cv.namedWindow("Result", cv.WINDOW_NORMAL)
cv.resizeWindow("Result", 1500, 1200)  # Pencerenin boyutunu ayarlayın.
cv.imshow("Result", show_img)
cv.waitKey(0)
cv.destroyAllWindows()
