f = open('./27_B_7627.txt')
k = int(f.readline())
n = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

mleft, mx = 0, 0
for i in range(n-k):
    mleft = max(mleft, t[i])
    mx = max(mx, mleft+t[i+k])
print(mx)  # 18469835
