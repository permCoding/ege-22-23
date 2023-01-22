# https://inf-ege.sdamgia.ru/problem?id=15124
def f(x,y,z):  # (x ≡ y ) ∨ ((y ∨ z) → x)
    return (x==y) or ((y or z) <= x)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if not(f(x,y,z)):
                print(x,z,y)
# 0 1 0
# 0 1 1