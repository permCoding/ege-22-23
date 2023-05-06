f = open('27_B_7627.txt')

k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mx, ma = 0, 0
for i in range(k, n):
    a, b = t[i-k], t[i]
    ma = max(ma, a)
    mx = max(mx, ma+b)

print(mx)  # ______
