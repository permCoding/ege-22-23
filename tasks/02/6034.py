def f(x,y,z,w):
    return not((w or (1-y)) and x) or (y==z)
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    print(w,x,z,y)