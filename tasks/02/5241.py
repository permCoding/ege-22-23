def f(x,y,z,w):  # (z ≡ ¬x) → ((w → ¬y) ∧ (y → x))
    return (z==(1-x)) <= ((w<=(1-y)) and (y<=x))

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(y,z,x,w)
"""
-0-
1 1 0 0

1 1 0 1
0 1 1 1

-1-
1 0 1 1
1 1 1 0
"""