def get(x):
    cnt = 0
    for j in range(1, round(x**.5)+1):
        if x%j==0: cnt +=2
        if j==x//j: cnt -=1
    return cnt


for i in range(1, 10**7+1):
    s = str(i)
    if s[0]=='3' and s[-3:-1]=='52':
        k = get(i)
        if k%2 != 0: print(i, k)

# print(get(3143529))
