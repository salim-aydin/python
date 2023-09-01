list_store = [1,2]

def add_element(a,b):
    c = a * b
    list_store.append(c) #local'den globali etkiledik
    print(list_store)


add_element(1, 9)

