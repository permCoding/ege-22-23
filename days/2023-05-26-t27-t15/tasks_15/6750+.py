def f(a, x, y):
    return (x+y<=32) or (y<=x+4) or (y>=a)

for a in range(300, 0, -1):
    if all(f(a,x,y) for x in range(1, 300) for y in range(1, 300)): 
        print(a)
        break
