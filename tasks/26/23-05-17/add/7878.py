f = open('./27A_7878.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(e) for e in f]

sm = 10**20
for i in range(n-1):
    for j in range(i+1, n):
        if j-i >= k:
            if (t[i]*t[j])%157 == 0:
                sm = min(sm, t[i]*t[j])
print(sm)
