def F(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

a = F(2023)
b = F(2020)
print(a,b,a/b)
        
