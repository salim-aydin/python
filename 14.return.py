def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)  # * 10 diyemezsin, return kullanman lazım


###Fonksiyonların çıktılarını , girdi olarak kullanabilmek için,
###return kullanılmaktadır ...


def calculate1(varm, moisture, charge):
    return (varm + moisture) / charge
    ##Gövdeye kod yazmaya devam etsen bile
    ##return'u gördüğü an buradan çıkar ...


cikti = calculate1(98, 12, 89) * 10
print(cikti)




def calculate2(varm, moisture, charge):
    varm = varm*2
    moisture = moisture * 2
    varm = varm * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


cikti2 = calculate2(98, 12, 78)
print(cikti2) # (392, 24, 89, 4.674157303370786) TUPLE , olarak döner


###############
###############
#veyaaaaaaaaaaaaaa

def calculate3(varm, moisture, charge):
    varm = varm*2
    moisture = moisture * 2
    varm = varm * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output

varm, moisture, charge, output = calculate3(98,12,78)
print(varm)
print(moisture)
print(charge)
print(output)


