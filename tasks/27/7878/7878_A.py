f = open('./27A_7878.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))
mn = 10**50
for i in range(n):
    for j in range(n):
        if j-i>=k:
            p = t[i]*t[j]
            if p%157==0: mn = min(mn, p)
print(mn)
