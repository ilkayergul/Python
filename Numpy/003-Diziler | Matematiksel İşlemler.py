a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)   #[5 7 9]
print(a-b)   #[-3 -3 -3]
print(a**2)  #[1 4 9]

# dizinin elemanlarını toplama
print(np.sum(a)) #6

# dizinin en büyük değeri
print(np.max(a)) #3

# dizinin en küçük değeri
print(np.min(a)) #1

# dizinin ortalama değeri
print(np.mean(a)) #2

# dizinin medyanı
# Eleman sayısı tek sayı ise ortadaki sayıyı, çift sayı ise ortadaki sayıların ortalamasını verir.
print(np.median(a)) #2

# [0,1] arasında rastgele sayı üretme
rndm = np.random.random((3,3))

# Dizinin tersini alma
print(a[::-1])

nums2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# 1. sütun ve tüm satırları alma
print(nums2d[:,1]) #[2 7]

# dizinin son satırı ve tüm sütunlarını alma
print(nums2d[-1,:]) #[6 7 8 9 10]

# diziyi vektör haline getirme
vector = nums2d.ravel() #[1 2 3 4 5 6 7 8 9 10]

# maksimum sayının index numarasını getirme
maxNumIndex = vector.argmax() #9







