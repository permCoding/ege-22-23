def f(a, x):
    return (x%a==0) or ((50<=x<=70) <= (x%16!=0))

for a in range(1, 1000):
    if all(f(a,x) for x in range(1, 1000)):
        print(a)
        # break
