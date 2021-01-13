import cv2

# Dosya yolu yazılır.
img = cv2.imread("image.jpg")

# Resmi siyah beyaz (grayscale) aktarmak için 0 yazılır.
img = cv2.imread("image.jpg", 0)

# Görselleştirme
cv2.imgshow("Resim Adi", img)

# Esc tuşuna basıldığında resim kapanır.
# s tuşuna basıldığında resim kaydedilir ve kapanır.
close_key = cv2.waitKey(0) &0xFF 
if  close_key == 27:
  cv2.destroyAllWindows()
elif close_key == ord('s'):
  cv2.imwrite("image_gray.png", img)
  cv2.destroyAllWindows()
  






