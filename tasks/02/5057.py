def f(x,y,z,w):  # (w → (y ≡ z)) ∧ (y ≡ (z → x))
    return (w <= (y==z)) and (y == (z<=x))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    print(z,w,y,x)
"""
-1-
0 1 0 0
0 0 1 0

0 0 1 1
0 1 1 1

-0-

0 0 0 1
1 0 0 0
"""