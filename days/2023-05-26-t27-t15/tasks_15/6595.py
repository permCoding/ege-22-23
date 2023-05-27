def f(a, x):
    return ((x%3==0) <= (x%2!=0)) or (x-a>=4)

for a in range(900, 0, -1):
    if all(f(a,x) for x in range(1, 900)):
        print(a)
        break
