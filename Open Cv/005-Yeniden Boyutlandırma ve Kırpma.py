# Görüntü işleme, nesne tespit, nesne takip gibi işlemlerde görüntü boyutlarını değiştirmeye ihtiyaç duyulur.
# Resim çok büyük ise kırpma ve boyutlarında düzenleme yapılabilir.

import cv2

img = cv2.imread("image.jpg")
print("Resim boyutu:", img.shape) #(512, 512)

# Yeniden boyutlandırma
imgResized = cv2.resize(img, (256,256))

# Kırpma işlemi
# 0 dan 100 e kadar olan pikseller alınır. Yükseklik.
# 0 dan 200 e kadar pikseller alınır. Genişlik
#Görüntü kareden dikdörtgene çevrilir.
imgCropped = img[:100,:200 ] 



