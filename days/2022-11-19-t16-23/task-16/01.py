import sys


sys.setrecursionlimit(2500)

def F(n):
    if n == 1: return 1
    return n * F(n-1)

print(len(str(F(2020))))
# 1 2 3 4 ... 2019 2020 2021 2022 2023
# 1 2 3 4 ... 2019 2020