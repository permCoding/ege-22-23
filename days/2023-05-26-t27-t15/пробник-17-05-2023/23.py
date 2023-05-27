def get(n , k):
    if n == 12: return 0
    if n > k: return 0
    if n == k: return 1
    return get(n+1,k) + get(n+2,k) + get(n*2,k)
    

print(get(2, 9) * get(9, 17))
