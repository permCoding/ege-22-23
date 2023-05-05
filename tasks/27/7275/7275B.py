f = open('27_B_7275.txt')
n, m = map(int, f.readline().split())
t = [0] * 10_000_000  # B

for _ in range(n):
    line = f.readline()
    pair = line.split()
    a, b = int(pair[0]), int(pair[1])
    b = (b-1)//30+1
    t[a] = b

mx = 0
i = m
sm = sum(t[i-m:i+m+1])
if t[i] != 0: mx = sm

for i in range(m+1, len(t)-m):
    sm += t[i+m] - t[i-m-1]
    if t[i] != 0: mx = max(mx, sm)
print(mx)  # 27140
