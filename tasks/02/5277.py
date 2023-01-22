def f(x,y,z,w):  # ¬(w ≡ y) ∧ (z → w) ∧ ¬x
    return not(w==y) and (z<=w) and (1-x)

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(z,x,w,y)