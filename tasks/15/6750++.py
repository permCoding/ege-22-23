def f(A,x,y):
    return (x+y<=32) or (y<=x+4) or (y>=A)

t = []
for A in range(1, 500):
    u = True
    for x in range(1, 500):
        for y in range(1,500):
            if f(A,x,y) == False: 
                u = False
                break
        if u == False: break
    if u == True:
        t.append(A)
print(max(t))
