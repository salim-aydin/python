#Methodlar, sınıflar içerisinde tanımlanan fonksiyonlardır...

int_methodlari = dir(int)
print(int_methodlari)

string_methodlari = dir(str)
print(string_methodlari)

###########################
###########################
###########################
###########################
###########################
###########################
###########################
###########################
###########################

int_methodlari = dir(int)
print("int metodları:")
for method in int_methodlari:
    print(method)

print("\nstring metodları:")
string_methodlari = dir(str)
for method in string_methodlari:
    print(method)



#########
#########
# __ başlamayanlar, ilgili veri yapısı ile birlikte kullanılabilecek methodlardır...

# len , bir gömülü fonksiyondur... __len__ ile belirtilir ...
# len , methodları string'lere uygulanabilmektedir...

name = "john"
name_tip = type(name)
print(name_tip) # <class 'str'>

len_tip = type(len)
print(len_tip) # <class 'builtin_function_or_method'>

name_boyut = len(name)
print(name_boyut) # 4

print(len("kaç karakterden oluşuyorsa onu yazdırır"))

########################################
########################################
########################################
########################################
########################################
########################################
########################################
# len bir fonksiyondur
# python'un , builtins.py 'nin içerisinde gömülü bir fonksiyonudur...

# fonksiyonlar bağımsızdır
# method'lar , class'larına özgüdür, onlar ın tipinde olduğunda , . nokta diyerek kullanılır


# upper() , lower(), küçük büyük dönüşümleri ...

miuul = "miuul"

buyult = "miuul".upper()  #anladın mı inceliği
buyult2 = miuul.upper()   #anladın mı inceliği

print(buyult)
print(buyult2)


kucult = buyult.lower()
kucult2 = buyult2.lower()

print(kucult)
print(kucult2)



######
# replace(arguman11, arguman22)
# replace(arguman11, arguman22)
# replace(arguman11, arguman22)
###  arguman11 der ki , değiştirmek istediğin ifadeyi gir
### arguman22 der ki , neyle değiştirmek istediğini girmen lazım ...


hi = "Hello AI Era"
degisti = hi.replace("l", "p")

print(degisti)




##########
#split , böler
#########
bol_kanka = "Hello AI Era".split() # ön tanımlı değeri boşluktur, boşluk görürse böler

a_ya_gore_bol = "Hello AI Era".split('a')


print(bol_kanka) # ['Hello', 'AI', 'Era']
print(a_ya_gore_bol) # ['Hello AI Er', '']


##################
## Kırpma işlemi, ön tanımlı olarak boşluğa göre kırpar
kirp1 = "      ofofo                   ".strip()
kirp2 = "ofofo".strip("o")
print(kirp1) #ofofo
print(kirp2) #fof


### capitalize() , ilk harfi büyütür
print("salim".capitalize())
