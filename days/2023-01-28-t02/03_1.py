def f(x,y,z,w):  # досрок 2022 2.1
    return not(x<=w) or (y==z) or y
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w) == False:
                    print(y,x,w,z)
