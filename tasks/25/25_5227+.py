def get(x):
    for j in range(2, round(x**.5)+1):
        if x%j==0: 
            return x//j


j = 1
while j < int((10**7)**.5)+1:
    i = j*j
    s = str(i)
    if s[0]=='3' and s[-3:-1]=='52':
        print(i, get(i))
    j += 1
# print(get(3143529))
