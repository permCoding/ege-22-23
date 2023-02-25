from itertools import permutations as perm

k = 0
for elm in perm('ГЕОРГИЙ'):
    if 'ГГ' not in "".join(elm):
        k += 1
print(k//2)


v1 = 'ГГОРЕИЙ'
v2 = 'ГГОРЕИЙ'
v1 == v2

##12
##21

##123
##132
##213
##231
##312
##321
