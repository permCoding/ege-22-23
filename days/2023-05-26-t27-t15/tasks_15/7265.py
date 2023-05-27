def f(a, x):
    return ((x%2==0) <= (x%3!=0)) or (x+a>=100)

for a in range(1, 1000):
    if all(f(a,x) for x in range(1, 1000)):
        print(a)
        break
