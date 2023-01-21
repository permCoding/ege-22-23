# https://inf-ege.sdamgia.ru/problem?id=18614

#  ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w)

def f(x,y,z,w):
    a = w <= (1-x)
    b = z <= y
    c = y or w
    return (a == b) and c

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    if x+y+z+w >= 0:
                        print(x,y,z,w)
"""
x w y z <-- решение
s=1
1 1 1 0 +
s=2
0 1 1 0
0 0 1 1 +
1 0 1 0
s=3
0 1 0 0 ~
0 0 1 0
0 1 1 1
1 1 0 1 ~
1 0 1 1

вывод по отдельности
y x z w
s=1
1 1 0 1 +
s=2
0 1 0 1
0 1 1 0 +
1 1 0 0
s=3
0 0 0 1
0 1 0 0
0 1 1 1
1 0 1 1
1 1 1 0
"""