# Try-Except Kullanımı

# Genel hata yakalama yöntemi.
try:
    1/0
except:
    print("Bir hata oldu.")

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
    
# Fonksiyon içerisinde hata yönetimi.    
# Fonksiyon içerisindeki hata raise ile gönderilir.
def kdv_rate(x):
    x = int(x)    
    if x < 0:
        raise ValueError("Negatif değer girilemez")
    return x * 0.18

# Raise ile gönderilen hata except ValueError üzerinden yakalanır ve değer e değişkenine atanır.
try:
    z = kdv_rate(-2)
    print(z)
except ValueError as e:
    print(e) #Negatif değer girilemez
    
    
# Custom Hata Yönetimi
class PasswordCompareExcept(Exception):
    pass

def password_compare(password, retry_password):
    if password != retry_password:
        raise PasswordCompareExcept("Girilen şifreler eşit değil.")
    return True

# Try-Except kullanmadan
# Hataya düşer ise program devam etmez
password_status = password_compare(123, 1234)
print(password_status) #PasswordCompare: Girilen şifreler eşit değil.

# Try-Except kullanarak.
try:
    password_status = password_compare(123, 1234)
except PasswordCompareExcept as e:
    print(e) #Girilen şifreler eşit değil.
