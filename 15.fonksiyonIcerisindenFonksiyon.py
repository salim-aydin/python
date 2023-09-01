

def calculate(varm, moisture, charge):
    return int((varm+ moisture) / charge)

calculate(90,12,12)*10


def standartdization(a,p):
    return a * 10 / 100 * p * p


sonuc = standartdization(45,1)
print(sonuc)


###############################
def all_calculationn(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standartdization(a, p)
    print(b*10)

all_calculationn(1,3,5,12)

################################

def all_calculationn2(varm, moisture, charge,a, p):
    print(calculate(varm, moisture, charge))
    b = standartdization(a, p)
    print(b*10)

all_calculationn2(1,3,5,12,20)

