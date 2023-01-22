# https://inf-ege.sdamgia.ru/problem?id=18781
def f(x,y,z,w):  # (¬x ∨ ¬y) ∧ ¬(x ≡ z) ∧ w
    return (not(x) or not(y)) and not(x==z) and w

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(w,x,y,z)
"""
1 0 0 1
1 0 1 1
1 1 0 0
"""