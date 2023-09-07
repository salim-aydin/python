#Birden fazla kod satırı ile yapılabilecek işlemleri,
# Kolayca tek bir satırda yapmak için kullanılır...


###KLASİK YOL

salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))


#############################
null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

print(null_list)


####
#Maaşlar, 3000 den küçükse başka işlem, 3000 den büyükse başka işlem yap...
print("----------------")
print("----------------")
print("----------------")

salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x * 20 / 100 + x

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))
print(null_list)


#####YUKARIDAKİ İŞLEMİ TEK BİR SATIRDA ÇÖZMEK İÇİN

[new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary <3000]


[salary * 2 if salary < 3000 else salary*0 for salary in salaries]

[new_salary(salary*2) if salary < 3000 else new_salary(salary*0.2) for salary in salaries]


#-----------------------
#-----------------------

students = ["John","Mark","Venessa","Mariam"]
students_no = ["John","Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

######################
[student.upper() if student not in students_no else student.lower() for student in students]