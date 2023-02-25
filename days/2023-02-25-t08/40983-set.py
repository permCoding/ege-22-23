from itertools import permutations as perm

k = set()
for elm in perm('ГЕОРГИЙ'):
    s = "".join(elm)
    if 'ГГ' not in s:
        k.add(s)
print(len(k))
