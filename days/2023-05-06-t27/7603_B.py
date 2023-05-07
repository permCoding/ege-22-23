f = open('27_B_7603.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

sm, ma = 0, 0
for i in range(k, n):  # b
    ma = max(ma, t[i-k])
    sm = max(sm, ma+t[i])

print(sm)  # 3094684
