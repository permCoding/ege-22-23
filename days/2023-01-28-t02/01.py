def f(x,y,z,w):
    return not(y<=(x==w)) and (z<=x)
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w):
                    print(x,y,z,w)
                
