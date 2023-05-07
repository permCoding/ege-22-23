f = open('27_A_7603.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

sm = 0
for i in range(n-k):  # a
    for j in range(i+k, n):  # b
        sm = max(sm, t[i]+t[j])

print(sm)  # 174902
