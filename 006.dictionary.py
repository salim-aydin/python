#Sözlük (Dictionary)

#Değiştirilebilir
#Sırasızzzzz( 3.7. versiyonundan sonra sıralı özelliği de eklenmiştir)
#Kapsayıcıdır(her türlü veri yapısını aynı anda ekleyeblirsin)

#key - value

dictionaryy = {"REG": "Regression"}

print(dictionaryy)
print(dictionaryy["REG"])


dictionaryy2 = {"REG": "Regression",
                "LOG": "Logistic Regression",
                "CART": "Classification and Reg"
                }
print(dictionaryy2["LOG"])
print(dictionaryy2["CART"])



dictionaryy3 = {"REG": ["RMSE",10],
                "LOG": ["MSE",20],
                "CART": ["SSE",30]
                }

print(dictionaryy3["LOG"])
print(dictionaryy3["CART"][1])



##########################
##########################
#KEY SORGULAMA
#KEY SORGULAMA
#KEY SORGULAMA
#KEY SORGULAMA
#KEY SORGULAMA
#KEY SORGULAMA

sorgu = "LOG" in dictionaryy3
sorgu2 = "salim" in dictionaryy3

print(sorgu)
print(sorgu2)


degeri_getir = dictionaryy3.get("LOG")  ### (self, key) , # key gireceksin
print(degeri_getir)


################################
################################
################################
dictionaryy3 = {"REG": ["RMSE",10],
                "LOG": ["MSE",20],
                "CART": ["SSE",30]
                }

### value değiştirme

dictionaryy3["REG"] = ["YSA", 10]
print(dictionaryy3)
print(dictionaryy3["REG"])


##tüm key'lere erişmek

keyleri_getir = dictionaryy3.keys()
print(keyleri_getir) #dict_keys(['REG', 'LOG', 'CART'])


#tüm value'lara erişmek

valuelari_getir = dictionaryy3.values()
print(valuelari_getir) # dict_values([['YSA', 10], ['MSE', 20], ['SSE', 30]])


##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
##########################
#Tüm Çiftleri TUPLE Halinde Listeye ÇEVİRME

key_ve_value_getir = dictionaryy3.items()
print(key_ve_value_getir) # TUPLE FORMUNDA GELDİ


#Value değerini değiştirmek için

dictionaryy3.update({"REG":111})
print(dictionaryy3)


#Yeni KEY-VALUE Eklemek için

dictionaryy3.update({"RF":10})
print(dictionaryy3)


# Varsa değiştirir , yoksa yeni atama yapar ,
# update methodu
