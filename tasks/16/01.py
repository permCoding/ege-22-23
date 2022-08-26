def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


a = fact(2023)
b = fact(2020)

print(a, b, a/b)
