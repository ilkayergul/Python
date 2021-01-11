# iterasyon - yineleme
# Değerler bellekte tutulur. Liste boyutu fazla olduğunda bellekte hafıza sorunu yaşanır.
liste = [1,2,3]
for i in liste:
    print(i)
    
    
# generator - yineleyiciler
# Değerler bellekte saklanmaz. Yeri geldiğinde üretilirler.

generator = (x for x in range(1,9))
for i in generator:
    print(i)
    
    
# yield 
# Fonksiyon generator döndürme işlemini return yerine yield ile yapar.
def createGenerator():
    liste = range(1,9)
    for i in liste:
        yield i
        
generator = createGenerator()
for i in generator:
    print(i)
