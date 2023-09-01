# True, False'u hatırlayalım

isBool1 = 1 == 1
isBool2 = 2 == 1

print(isBool1)
print(isBool2)

if 1 == 1:
    print("1 ' 1 e eşittir")

if 1 == 2:
    print("bu yazı print'te görünmeyecek")

number = 11

if number == 10:
    print("number 11, 10 'a eşit değil , o yüzden")
    print("burası da yazmayacak")


def number_check(number):
    if number == 10:
        print("number is 10")

number_check(11)
number_check(12)
number_check(13)
number_check(10)


