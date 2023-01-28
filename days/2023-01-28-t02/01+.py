for x in 0,1: # demo 2022
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(y<=(x==w)) and (z<=x):
                    print(w,x,y,z)
            
