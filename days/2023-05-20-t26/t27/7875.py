f = open('./27A_7875.txt')
n = int(f.readline())
k = int(f.readline())
t = list(map(int, f))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if j-i >= k:
            x = (t[i]*t[j])%7==0
            y = (t[i]+t[j])%2==0
            if x and y:
                cnt += 1
print(cnt)
