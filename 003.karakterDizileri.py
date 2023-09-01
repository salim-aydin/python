#Strings

print("John")

name = "salim"

print(name)


### Çok satırlı karakter dizileri
paragraf_satiri = """sanırım hizalı bir şekilde
yazılanları gösteriyor
ama emin değilim
"""

print(paragraf_satiri)


# String aslında bir char dizisidir
yazi = "selam kanka"

print(yazi[0])
print(yazi[1])
print(yazi[2])
print(yazi[3])
print(yazi[4])



#Karakter Dizilerinde Slice İşlemi
#Yani dilimleme İşlemi
print(yazi[0:5]) # yukarıdaki yaptığım işlemin, kısa haliiiii
# 0 dan başla , 5 e kadar git, 5 dahil değiiiiiiil



#String içerisinde karakter sorgulamak

cumle  = "Veri yapıları hızlı özet"
aktarma = "veri" in cumle # veri ifadesi içinde mi cümlenin ?
print(aktarma) # False


aktarma1 = "Veri" in cumle
print(aktarma1) # True # Veri içinde mi cumle nin

aktarma2 = "yapıları" in cumle
print(aktarma2) # True # yapıları içinde mi cümle nin




#Bir satır aşağıda başlatmak için

satir = "Tüm\nsatırlar\ndize\nhalinde\nolacak"
print(satir)







