def f(A,x):
    a = (x&39==0)
    b = (x&11==0)
    c = not(x&A==0)
    return a or (b <= c)

for A in range(1, 900):
    t = [f(A,x) for x in range(1, 900)]
    if all(t): 
        print(A)
        break

# print(14 & 5)