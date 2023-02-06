def f(x,y,z,w):
    return not(z or (w<=y)) or (x<=z)
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    print(z,w,y,x)