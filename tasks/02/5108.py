def f(x,y,z,w):  # ¬(w → x) \/ (y → z) \/ ¬y
    return not(w<=x) or (y<=z) or (1-y)
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    print(z,w,y,x)