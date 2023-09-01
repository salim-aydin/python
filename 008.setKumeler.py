#Set

# Değiştirilebilir
# Sırasız + Eşsizdir
# Kapsayıcıdır...


###############
# difference() : İki kümenin farkı

set1 = set([1,3,5])
set2 = set([1,2,3])


#set1 'de olup set2'de olmayanlar ...
fark = set1.difference(set2)
print(fark)



##################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar...

toplam_farklari = set1.symmetric_difference(set2)
print(toplam_farklari)



##############
# intersection() :  İki kümenin kesişimi
set1 = set([1,3,5])
set2 = set([1,2,3])

kesisim = set1.intersection(set2)
print(kesisim)


################
################
# Kısa yollar
# fark , set1-set2
# kesisim , set & set2

kisa_yol_fark = set1 - set2
print(kisa_yol_fark)

kisa_yol_kesisim = set1 & set2
print(kisa_yol_kesisim)



#################
# union() iki kümenin birleşimi

birlesme = set1.union(set2)
print(birlesme)



###############
# isdisjoint() : iki kümenini kesişimi boş mu ?

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

kesisim_yok = set1.isdisjoint(set2)
print(kesisim_yok)



#issubset() : bir  kime diğer kümenin alt kümesi mi ?
alt_kume_mi = set1.issubset(set2)
print(alt_kume_mi)



#issuperset() : bir küme diğer kümeyi kapsıyor mu?
kapsiyor_mu = set2.issuperset(set1)
print(kapsiyor_mu)


