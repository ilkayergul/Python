import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Horizontal birleştirme (yatay)
horizontal_img = np.hstack((img,img))

# Vertical birleştirme (dikey)
vertical_img = np.vstack((img,img)) 

