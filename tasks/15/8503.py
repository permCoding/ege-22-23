def f(a,x):
    return ((x & 52 != 0) and (x & 36 == 0)) <= int(not((x & a) == 0))

for a in range(1000):
    for x in range(1000):
        if f(a,x) == False:
            break
    else:
        print(a)
        break
