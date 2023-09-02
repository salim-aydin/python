# Amaç aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN


#Çift index büyük
#Tek index küçük


boyut_bilgisi = len("miuul")
print(boyut_bilgisi)

range_aktardim1 = range(boyut_bilgisi) # alttakiyle aynı
range_aktardim2 = range(0,5)           # üsttekiyle aynı

print(range_aktardim1)
print(range_aktardim2)


##########Python'consol'da yazdır daha kolay olur
range(len("miuul"))
range(0,5)

for i in range(0,5): # 0 dan 5 ee kadar
    print(i)


for i in range(len("miuul")):
    print(i)



def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("zafer")




def alternating1(string):
    new_string = ""
    for string_index in range(len(string)): #girilen string'in index'lerinde gez
        if string_index % 2 == 0: # index çift ise , for'dan gelen o index'i büyült
            new_string += string[string_index].upper()
        else: # index tek ise , for'dan gelen o index'i küçült
            new_string += string[string_index].lower()
    print(new_string)


alternating1("kanks çıkıyoz mu ")