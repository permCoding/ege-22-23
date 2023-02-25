from itertools import permutations as perm
from itertools import combinations as comb
from itertools import product as prod

lst = list('abcd')  # ['a', 'b', 'c', 'd']
# print(lst)

# for elm in perm(lst): print(elm)

# for elm in comb(lst, 2): print(elm)

##for count in range(len(lst)+1):
##    for elm in comb(lst, count):
##        print(elm)

for elm in prod(lst, repeat=2):
    s = "".join(elm)
    print(s)    
