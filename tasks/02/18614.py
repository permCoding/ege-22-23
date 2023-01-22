# https://inf-ege.sdamgia.ru/problem?id=18614

def f(x,y,z,w):  # ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w)
    return ((w<=(1-x)) == (z <= y)) and (y or w)


for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(x,w,y,z)
"""
-1-
0 0 1 1

0 1 0 0

0 0 1 0
0 1 1 0
1 0 1 0

-0-
1 1 1 0
"""