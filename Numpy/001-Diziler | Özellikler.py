# Numpy matrisler için hesaplama kolaylığı sağlar.

#Numpy kütüphanesi kullanımı
import numpy as np

# 1*9 boyutunda dizi oluşturma
numbers = np.array([1,2,3,4,5,6,7,8,9])

# Dizinin özellikleri
print("Şekil:", numbers.shape)          #Şekil: (9, )
print("Boyut:", numbers.ndim)           #Boyut: 1
print("Veri Tipi:", numbers.dtype.name) #Veri Tipi: int32
print("Boy:", numbers.size)             #Boy: 9

# Numbers dizisi 2 boyutlu diziye çevrilir.
numbers2d = numbers.reshape(3,3)

# Dizinin tipini öğrenme
print(type(numbers2d))  #<class 'numpy.ndarray'>

### <--- !!! Önemli
# ??? Dizi numpy olmadan oluşturulup 2 ile çarpıldığında dizinin elaman sayısı iki katına çıkar.
nums2d = [[1,2,3],[4,5,6],[7,8,9]]
print(2*nums2d) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ??? Dizi numpy ile oluşturulup 2 ile çarpıldığında dizinin elemanlarının değeri iki katına çıkar.
nums2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(2*nums2d) #[[ 2  4  6],[ 8 10 12],[14 16 18]]
### -->

# Arange metodunun kullanımı
arange = np.arange(10,50,5)

# Linspace metodunun kullanımı
linspace = np.linspace(10,20,5) #[10,12.5,15,17.5,20]






