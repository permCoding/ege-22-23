def f(A,x,y):
    return (x+y<=32) or (y<=x+4) or (y>=A)

for A in range(500, 0, -1):
    for x in range(1, 500):
        t = [f(A,x,y) for y in range(1,500)]
        if not(all(t)): break
    else:
        print(A)
        break
