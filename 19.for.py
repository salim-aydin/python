students = ["John", "Mark", "Venessa", "Mariam"]

print(students)

print(students[0])
print(students[1])
print(students[2])
print(students[3])

print("---------------------")
print("---------------------")
print("---------------------")

# for in students , döngüyü nereden gerçekleştireceksin ?
# for temsilEt    , her bir eleman gezilirken, bununla temsil edilecek
for donenleriTemsilEt in students:
    print(donenleriTemsilEt)

print("---------------------")
print("---------------------")
print("---------------------")

for donenleriTemsilEt2 in students:
    print(donenleriTemsilEt2.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

print("---------------------")
print("---------------------")
print("---------------------")

for salary in salaries:
    print(salary * 1.20)

print("---------------------")
print("---------------------")
print("---------------------")

for salary in salaries:
    print(salary * 20 / 100 + salary)

print("---------------------")
print("---------------------")
print("---------------------")


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


sonuc1 = new_salary(1500, 10)
sonuc2 = new_salary(1000, 50)

print(sonuc1)
print(sonuc2)

print("---------------------")
print("---------------------")
print("---------------------")


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 20))



##########################
##########################
##########################
##########################
##########################
# Maaşı 3000den az olanlara farklı
# 3000 den fazla olanlara farklı işlem yapacağız



def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

salaries2 = [1000,2000,3000,4000,5000,6000]

for salary in salaries2:
    if salary >= 3000:
        print(new_salary(salary,15))
    else:
        print(new_salary(salary, 20))