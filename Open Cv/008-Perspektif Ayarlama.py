import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Dönüştürülecek resim boyutları
width = 600
height= 700


# Çapraz bir resmin köşe pikselleri tespit edilir.
points_1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
points_2 = np.float32([[0,0], [0, height], [width,0], [width,height]])

# Perspeftif alma
matrix = cv2.getPerspectiveTransform(points_1, points_2)

# Dönüştürülmüş resim
img_output = cv2.warpPerspective(img, matrix, (width,height))
cv2.imgshow("Yeni Resim", img_output)

