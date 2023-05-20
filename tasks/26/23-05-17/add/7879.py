f = open('./27A_7879.txt')
n = int(f.readline())
k = int(f.readline())
t = [int(e) for e in f]

sm = 0
for i in range(n-1):
    for j in range(i+1, n):
        if j-i >= k:
            if (t[i]+t[j])%2023 == 0:
                if (t[i]%47==0) ^ (t[j]%47==0):
                    sm = max(sm, t[i]+t[j])
print(sm)
