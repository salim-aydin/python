# Enumerate : Otomatik Counter/Indexer ile for loop
# Bir iteratif nesne içinde gezip elemanlarına bir şey yaparken ;;;
# Aynı zamanda o elemanların , index bilgilerinide takip etmek istediğimizde yaparız...



students = ["John","Mark","Venessa","Mariam"]
#indexi çift olanlara başka, tek olanlara başka bir işlem yapacağız
# range ve len 'ile de index üretebileceğim gibi,
# buradaki iteratif nesnenin sahip olduğu index bilgisiyle de bunu gerçekleştirebilirim

for student in students:
    print(student)


for index, student in enumerate(students):
    print(index,student)


for index, student in enumerate(students,1): # index 1 den başlasın
    print(index,student)

################################
################################
print("---------------------")
print("---------------------")
print("---------------------")
print("---------------------")


A = []
B = []
students = ["John","Mark","Venessa","Mariam"]

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

    print(A,B)

print("--------------------------")
print("--------------------------")
print(A,B)



