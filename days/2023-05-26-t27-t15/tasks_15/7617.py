def f(a, x, y):
    return (x>=9) or (2*x<y) or (x*y<a)

for a in range(1000):
    for x in range(1000):
        t = [f(a,x,y) for y in range(1000)]
        if not(all(t)): break
    else:  # если не было break
        print(a)
        break
