from itertools import product as prod

k = 0
for elm in prod('АБРТЫ', repeat=5):
    k += 1
    s = "".join(elm)
    if ('А' not in s) or ('Ы' not in s): continue
    if ('ЫА' in s) or ('АЫ' in s): continue
    print(elm, k)
    break
