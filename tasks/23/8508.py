def get(n, k):
    if n > k:return 0
    if n == 12:return 0
    if n == k: return 1
    a = get(n+1, k)
    b = get(n+2, k)
    c = get(n*2, k)
    return a+b+c

print(get(2,9)*get(9,17))  # 350
