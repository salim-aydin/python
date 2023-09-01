# def function_name(parameters/argumants):
#    statement ( function body)


def say_hi():
    print("merhaba")
    print("hi")
    print("hello")


say_hi()


def say_hi1(string):
    print(string)
    print("hi")
    print("hello")


say_hi1("kanks")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# Girilen değerleri bir liste içinde saklayacak fonksiyon...

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c) # append , kalıcı işlem yapar, o yüzden değişkene aktarmadık ...
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180,10)


