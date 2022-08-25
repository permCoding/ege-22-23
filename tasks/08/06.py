from itertools import product

def check(o):
    return o[0]!='0' and o.count('6')==1 and all(elm not in o for elm in lst)


count = 0
lst = ['16', '36', '56', '76', '67', '65', '63', '61']
for comb in product('01234567', repeat=5):
    if check(''.join(comb)):
        count += 1

print(count)
