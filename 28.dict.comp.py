dictionary = {'a':1 ,
              'b':2,
              'c':3 ,
              'd':4}


dictionary.keys()

dictionary.values()

dictionary.items()


degisken1 = dictionary.keys()
degisken2 = dictionary.values()
degisken3 = dictionary.items()

print(degisken1)
print(degisken2)
print(degisken3)


##################################
{k: v ** 2 for (k,v) in dictionary.items()}

{k.upper() : v **2  for (k,v) in dictionary.items()}