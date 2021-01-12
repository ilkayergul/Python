# Try-Except Kullanımı

# Girilen değer sayı değil ise ValueError exception ile yakalanır.
while True:
    x = input("Bir sayı giriniz: ")
    if not x:
        break;
    try:
        y = float(x)
    except ValueError:
        print("Geçersiz sayı")
        continue
    print(y**2)
    
# Birden fazla except kullanımı
while True:
    x = input("Bir sayı girin: ")
    if not x:
        break
    try:
        y = 1/float(x)
    except ValueError:
        print("Geçersiz sayı")
        continue
    except ZeroDivisionError:
        print("Sıfıra bölme")
        continue
    print(y)
