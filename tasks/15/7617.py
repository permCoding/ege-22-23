def f(A,x,y):
    return (x>=9) or (2*x<y) or (x*y<A)

for A in range(1, 900):
    for x in range(1, 900):
        t = [f(A,x,y) for y in range(1, 900)]
        if not(all(t)): break
    else:
        print(A)
        break
