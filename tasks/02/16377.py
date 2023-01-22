# https://inf-ege.sdamgia.ru/problem?id=16377
def f(x,y,z,w):  # ((x → y) ≡ (y → z)) ∧ (y ∨ w)
    return ((x<=y) == (y<=z)) and (y or w)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(x,z,w,y)
"""
_ _ w _
0 1 0 1
0 0 1 0 +
0 0 1 1

0 1 1 1
1 1 0 1

"""