def f(A,x):
    a = x%A==0
    b = 50<=x<=70
    c = x%16!=0
    return a or (b <= c)

for A in range(900, 0, -1):
    t = [f(A,x) for x in range(1, 900)]
    if all(t): 
        print(A)
        break

# print(14 & 5)