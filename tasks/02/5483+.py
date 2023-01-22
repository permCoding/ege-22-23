from itertools import permutations as p


def f(x,y,z,w):  # (z ≡ ¬x) → ((w → ¬y) ∧ (y → x))
    return (z == (1-x)) <= ((w<=(1-y)) and (y<=x))


rows = [[1,1,1,0],[2,2,0,0],[2,0,2,2]]
ress = [1,0,0]

for t in p([0,1,2,3]):
    row = rows[0]
    res = ress[0]
    e = [row[i] for i in t]
    x,y,z,v = row
    if f(x,y,z,v) == res:
        if e == row:
            print(t)

# это слишком трудоёмкий способ
"""
z y x w
z x y w

-1-
1 0 1 1 | True
1 1 1 0 | True +
-2-
0 1 1 0 | False +
-3-
0 1 1 0 | False
0 1 1 1 | False
1 1 0 1 | False +
"""