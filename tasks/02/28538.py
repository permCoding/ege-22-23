# https://inf-ege.sdamgia.ru/problem?id=28538
def f(x,y,z,w):  # ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)
    return ((x and y) <= ((1-z) or w)) and(((1-w)<=x) or (1-y))

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    print(z,w,y,x)
                