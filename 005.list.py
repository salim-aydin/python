#List
#Değiştirilebilir
#Sıralı(İndex işlemi yapılabilir)
#Kapsayıcı(Birden fazla veri yapısını bir arada tutabilir)

notes = [1,2,3,4]

tip = type(notes)
print(tip) # <class 'list'>


names = ["a","b","c","d","e"]
not_nam = [1,2,3,"a","b",True,[1,2,3]] #Kapsayıcı

secim1 = not_nam[0]
secim2 = not_nam[1]
secim3 = not_nam[2]
secim4 = not_nam[3]

print(secim1)
print(secim2)
print(secim3)
print(secim4)

secim_ic = not_nam[6][0] # listenini içerisindeki elemana erişmek
print(secim_ic)


not_nam[6][0] = 100

print(not_nam[6][0])

git = not_nam[0:4]

print(git)


# LİSTE METHODLARIIIIIIIIIIIIII
# LİSTE METHODLARIIIIIIIIIIIIII
# LİSTE METHODLARIIIIIIIIIIIIII

print(dir(not_nam))



int_methodlari = dir(int)
print("int metodları:")
for method in int_methodlari:
    print(method)


list_methodlari = dir(not_nam) # not_name bir liste olduğu için , şuan methodlarını dizi olarak, list_methodlari'na attım
print("liste methodları")
for method in list_methodlari:
    print(method)

##append 'i adın soyadın gibi bil :D

#append  , listlere eleman eklemek için kullanılır ...

print(len(list_methodlari))
print(len(not_nam))

print(not_nam)

not_nam.append(200)
not_nam.append(300)

print(not_nam)


########################
#pop
#index'e göre eleman silmek için kullanılır...

not_nam.pop(0)
not_nam.pop(0)
not_nam.pop(0)

print(not_nam)

###################
#insert : indexe ekler

not_nam.insert(0,100)
not_nam.insert(1,500)
not_nam.insert(2,999)

print(not_nam)










