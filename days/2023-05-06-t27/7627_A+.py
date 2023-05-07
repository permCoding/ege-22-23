f = open('27_A_7627.txt')

k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

sm = 0
for i in range(n-k):  # a
    for j in range(i+k, n):  # b
        sm = max(sm, t[i]+t[j])

print(sm)  # 19974
