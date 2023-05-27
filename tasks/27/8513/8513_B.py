f = open('./27_B_8513.txt')
k = int(f.readline())
n = int(f.readline())
t = list(map(int, f))

sma, sm = 0, 0
for i in range(n-k):
    sma = max(sma, t[i])
    sm = max(sm, sma+t[i+k])
print(sm)  # 2090920
