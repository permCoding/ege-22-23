def f(x,y,z,w):  # demo 2023
    return not(y<=x) or (z<=w) or not(z)
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    print(y,x,z,w)
