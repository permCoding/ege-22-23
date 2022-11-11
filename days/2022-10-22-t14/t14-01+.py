# https://inf-ege.sdamgia.ru/problem?id=7761

x = 4**2020 + 2**2017 - 15
b = bin(x)
count = 0
for smb in b:
    if smb == '1':
        count += 1
print(count)

'''
Сколько единиц содержится в двоичной записи 
значения выражения: 4**2020 + 2**2017 – 15?
2015
'''