f = open('./27T_7878.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))

mn = max(t)**2
for i in range(n):
    for j in range(n):
        if j-i>=k:
            p = t[i]*t[j]
            if p%157==0:
                mn = min(mn, p)
print(mn)