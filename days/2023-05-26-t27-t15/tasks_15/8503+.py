def f(a, x):
    return ((x & 52 !=0) and (x & 36 == 0)) <= int(not((x & a) == 0))

for a in range(1000):
    if all(f(a, x) for x in range(1000)):
        print(a)
        break
