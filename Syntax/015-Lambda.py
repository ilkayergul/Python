# Lambda bir fonksiyondur. Parametreler alabilir. Fonksiyondan dönen değer bir tanedir.
# Fonksiyonların içerisinde kullanılabilir.
# Tanımlanırken başına def yazılmaz.

# : olan kısıma kadar yazılan değerler parametredir.
get_kdv_rate = lambda x : x * 0.18
print(z(100)) #18.0

# Öncelikle normal fonksiyone parametre verilir. Sonrasında lambda fonksiyonuna parametre verilir.
# Yapılan işlem: x değeri x+1 ile çarpılır. ilk_islem e verilen parametre ise toplanır.
# 9 * (9+1) = 90
# 2 + 90 = 92
def carp(x):
  return lambda y : y + x * (x + 1)
  
ilk_islem = carp(9)
print(ilk_islem(2)) #92 

#Birden fazla parametreli kullanımı
x = lambda a, b, c : a + b + c
print(x(1,2,3)) #6
