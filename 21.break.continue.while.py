# break, akışı kes
# continue , akışı atla
# while   , akışa devam et


salaries = [1000, 2000, 3000 , 4000, 5000]


#break, aranan koşul sağlandığında akışı keser

for salary in salaries:
    if salary == 3000:
        break
    print(salary) # 1000 ve 2000 i yazar ,,,,,,,,,,,,,,, 3000 , 4000, ve 5000'i yazmazzzzzzzzzz

for salary in salaries:
    if salary == 3000:
        continue
    print(salary) # 3000 hariç hepsini yazar ...



# while , dığı sürece demektir

number = 1
while number < 5:
    print(number)
    number += 1



