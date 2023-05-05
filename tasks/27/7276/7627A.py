f = open('./27_A_7627.txt')

k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mleft, mx = 0, 0
for i in range(n-k):
    mleft = max(mleft, t[i-k])
    mx = max(mx, mleft+t[i])
print(mx)
# 19974
# 18469835