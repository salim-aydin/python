def summer(a, b):
    return a + b


degisken1 = summer(1, 3) * 9
print(degisken1)

# Lambda, kullan at fonksiyondur,
# veeeeeeeeeeee
# return kullanman gerekmiyooorr
new_sum = lambda a, b: a + b
print(new_sum(4, 5))

##########################

# map , bizi döngü yazmaktan kurtarır
# map , bizi döngü yazmaktan kurtarır
# map , bizi döngü yazmaktan kurtarır
# map , bizi döngü yazmaktan kurtarır
# bana içerisinde gezebileceğim, iteratif bir nesne ver,
# ve bu nesneye uygulamak istediğin fonksiyonu ver
# ben sana bu işlemi otomatik olarak yaparım der

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x

print(new_salary(1000))
print("------------")


for salary in salaries:
    print(new_salary(salary))

degisken2 = list(map(new_salary,salaries))
print(degisken2)



############################
############################
############################
############################
############################

print(list(map(lambda x: x*20 / 100 + x,  salaries)))




##############
#filter
# belirli koşulu sağlayanları seçmek istediğimiz zaman , ve sonra işlem yaptırmak için kullanırız

list_store = [1,2,3,4,5,6,7,8,9,10]
degisken3 = list(filter(lambda x : x % 2 == 0 , list_store))
print(degisken3)


#reduce , indirgemek demektir
from functools import reduce
list_store = [1,2,3,4]

degisken5 = reduce(lambda a,b:a+b, list_store)

print(degisken5)








