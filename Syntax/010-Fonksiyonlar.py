def kare(x):
  print(x**2)
kare(3)

# Return Kullanımı
def kare(x):
  return x**2
sonuc = kare(3)

# Birden fazla parametreli kullanımı. Parametreler default tanımlı.
def insan(yas='21', kilo=75):
  print("Yaş:",yas)
  print("Kilo:",kilo)
insan()

# Parametre sayısı belli değil ise * kullanılır.
# Parametre dizi gibi davranır. Parametreye index yardımıyla erişilir.
def students(*student):
  print("student[2]")

# Parametre sırasına göre girilmek istenmiyor ise (key,value) üzerinden erişim sağlanır.
def students(student1, student2, student3):
  return student1 + student2 + student3

students(student3 = "Mehmet", student2 = "Ali", student1 = "Veli")

# Parametrenin başına ** eklenirse dictionary gibi davranır.
def students(**student):
  print("Öğrencinin adı: " + student["name"])
  
students(age=20, name="Ahmet")

# Fonksiyon tanımlandığında içi boş bırakılamaz. Eğer içini sonradan doldurmak istersek pass komutu kullanılır.
def calc_kdv(x):
  pass

 
