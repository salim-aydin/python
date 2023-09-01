# ?print  , python console'ekranından sorgula, terminalden değil

# Parametre , method tanımlanırken
# argüman, method çağrıldığında girilen değerlerdir...

print("a", "b")

print("a", "b", sep="___")  # sep'in default değeri boşluk , " " biz bunu 3 alt çizgi ile değiştirdik

help(print)


# fonksiyon tanımlama

def calculate(x):
    print(x * 2)


calculate(5)


def summer(arg1,arg2):
    print(arg1+arg2)


summer(10,15)
summer(arg2=15, arg1=10)



