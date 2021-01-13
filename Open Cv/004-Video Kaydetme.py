# Veri toplamak için video kaydetme kullanılabilir.

import cv2

# Bilgisayar kamerasına ulaşmak için 0 kullanılır.
# Harici kamera var ise 1 değeri verilir.
cap = cv2.VideoCapture(0)

# Genişlik ve yükseklik değeri alınır.
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video kaydedici başlatma
# VideoWriter.fourcc() # Çerçeveleri sıkıştırmak için kullanılan 4 karakterli codec kodu.
# 20 = Saniyedeki resim sayısı.
writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))

while True:
  # Videodan gelecek frame(resimler)
  ret, frame = cap.read()
  cv2.imshow("Video", frame)
  
  #Kaydet
  writer.write(frame)
  
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
writer.relase()
cv2.destroyAllWindows()
