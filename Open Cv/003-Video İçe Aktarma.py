import cv2
import time

video_name = "video.mp4"

# Video içe aktar
cap = cv2.VideoCapture(video_name)

print("Genişlik:", cap.get(3)) #Video genişliği
print("Yükseklik:", cap.get(4)) #Video genişliği

# Video açılmadığında veya boş olduğunda 
if cap.isOpened() == False:
  print("Hata")

# Videoyu sürekli okuyabilmek için döngüye alınır.
while True:
  # Frame = Video içerisinde oynayan her bir resim
  # Return = İşlemin başarılı, başarısız olduğunu döner. (True,False)
  ret, frame = cap.read()

  if  ret == True:
    # Video hızlı aktığı için yavaşlatıyoruz.
    time.sleep(0.01)
    cv2.imgshow("Video:",frame)
  else: 
    break
    
  # Klavyeden q tuşuna basıldığında videodan çıkar.
  if  cv2.waitKey(1) & 0xFF == ord("q"):
    break
    
# Video yakalama bırakılır.
cap.relaese()
cv2.destroyAllWindows()

