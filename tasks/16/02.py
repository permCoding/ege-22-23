import sys

sys.setrecursionlimit(3000)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

a = fact(2023)
b = fact(2020)

print(a, b, a/b)
