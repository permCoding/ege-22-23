def f(A,x):
    return (x%A==0) or ((50<=x<=70) <= (x%16!=0))

for A in range(1, 1_000):
    t = [f(A,x) for x in range(1, 1_000)]
    if all(t): print(A)
