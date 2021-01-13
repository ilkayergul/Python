import cv2
import matplotlib.pyplot as plt

# Open cv kütüphanesi resimdeki renkleri rgb yerine bgr olarak algılar.
img_1 = cv2.imread("image1.jpg")
img_2 = cv2.imread("image2.jpg")

# RGB çevirme
img_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img_2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Karıştırma işlemi
# Karıştırılmış resim = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1 = img1, alpha= 0.5, src2 = img2, beta = 0.5, gamma = 0)

plt.figure()
plt.imshow(blended)
