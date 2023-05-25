def f(a,x):
    return ((x%3==0) <= (x%2!=0)) or (x-a>=4)

for a in range(500, 0, -1):
    t = [f(a,x) for x in range(1, 500)]
    if all(t):
        print(a)
        break
