def f(a, x, y):
    return (x+y<=32) or (y<=x+4) or (y>=a)

for a in range(1000, 0, -1):
    for x in range(1, 1000):
        t = [f(a,x,y) for y in range(1, 1000)]
        if not(all(t)): break
    else:
        print(a)
        break
