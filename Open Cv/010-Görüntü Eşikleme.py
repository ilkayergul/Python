# Resimdeki ana hatların ortaya çıkarılması sağlanır.

import cv2
import matplotlib.pyplot as plt

# Resmi içeri aktarma
img = cv2.imread("image1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #GrayScale convert

# Thresh ile maxval arasındaki değerler beyaz olur.
# cv2.THRESH_BINARY_INV uygulanırsa tam tersi olur. Yani beyaz yerine siyah olur.
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

# Uyarlamalı eşik değeri
# Bir dağ resminde bazı bölgerine ışık az düşer ise o bölge koyu renk olur. 
# Bu algoritmada dağı bir bütün olarak algılar ve renk dağılımını eşit uygular.
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

#Görselleştirme
plt.figure()
plt.imgshow(thresh_img2, cmap = "gray ")
plt.axis("off") #eksenler kapanır.
plt.show()
