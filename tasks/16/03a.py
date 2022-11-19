def F(n):
    if n == 0: return 0
    return F(n/2) if n % 2 == 0 else 1 + F(n-1)


##cnt = len([1 for n in range(1, 1001) if F(n) == 3])
cnt = [F(n) for n in range(1, 1001)].count(3)
print(cnt)
