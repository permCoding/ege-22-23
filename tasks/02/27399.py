# https://inf-ege.sdamgia.ru/problem?id=28538
def f(x,y,z,w):  # (x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w
    return (x or y) and not(y==z) and (1-w)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(z,y,x,w)
                