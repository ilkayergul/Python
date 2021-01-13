import cv2
import numpy as np

# Resim oluşturma
# 512x512 boyutlarında 3 boyutlu resim oluşturulur.
img = np.zeros((512,512,3), np.uint8) #Siyah resim

# Çizgi
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (0,0), (512,512), (0,255,0), 3)

# Dikdörtgen
# (resim, başlangıç noktası, bitiş noktası, renk, arkaplan)
cv2.rectangle(img, (0,0), (100,100), (255,0,0), cv2.FILLED)

# Circle
# (resim, merkez noktası, yarıçap, renk, arkaplan)
cv2.circle(img, (256,256), 45, (0,0,255), cv2.FILLED)

# Metin
# (resim, yazı, konum, font, kalınlık, renk )
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
