def f(a, x):
    return (x&39==0) or ((x&11==0) <= int(not(x&a==0)))

for a in range(1000):
    if all(f(a,x) for x in range(1000)):
        print(a)
        break

