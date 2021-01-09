# Demet(Tupple) içerisindeki elemanları değiştiremeyiz.

demet = (1,2,3,"Merhaba","Dünya)
print(demet)

demet2 = (10,11,12)

# Demet birleştirme
yeniDemet = demet+deneme2

# Belirtilen elemana ulaşma.
demet[0] #1

# Demet silme
del demet

# Demet içerisinde veri kontrolü
harfler = ("a","b","c","d","e","f")
"ç" in harfler #False
"e" in harfler #True
