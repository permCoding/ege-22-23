def get_a(k):
    n = len(t)
    sm = 0
    for i in range(n-k+1):  # n -> <=k
        tmp = 0
        for j in range(i, i+k):
            if j < n:
                tmp += t[j]
        sm = max(sm, tmp)
        print(tmp)
    return sm

def get_b(k):
    n = len(t)
    sm = tmp = sum(t[0:k])
    for i in range(1, n-k+1):  # n -> <=k
        tmp = tmp - t[i-1] + t[i+k-1]
        sm = max(sm, tmp)
    return sm

t = [-2,3,-2,0,1,-5,4,2]
k = 2
print(get_a(k), get_b(k))
