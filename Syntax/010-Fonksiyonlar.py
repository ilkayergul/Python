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

