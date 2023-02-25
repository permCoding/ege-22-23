# https://inf-ege.sdamgia.ru/problem?id=37143
from itertools import product as prod
k = 0
for elm in prod('ГЕПАРД', repeat=5):
    if elm.count('Г')==1:
        if elm[0]!='А':
            if elm[-1]!='Е':
                k += 1
print(k)
