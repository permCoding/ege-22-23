# https://inf-ege.sdamgia.ru/problem?id=46960
def f(x,y,z,w):  # (¬y → (z ≡ w)) ∧ ((z → x) ≡ w)
    return ((1-y)<=(z==w)) and ((z<=x) == w)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(z,w,y,x)

"""
1 1 0 1
0 1 1 1
0 1 1 0

1 0 1 0
"""