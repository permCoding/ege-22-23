f = open('27_B_7275.txt')
n, m = map(int, f.readline().split())
t = [0] * 10**7  # B

for e in f:
    a, b = map(int, e.split())
    t[a] = (b+29)//30

mx = 0
sm = sum(t[0:2*m+1])
if t[m] != 0: mx = sm

for i in range(m+1, len(t)-m):
    sm += t[i+m] - t[i-m-1]
    if t[i] != 0: mx = max(mx, sm)
print(mx)  # 27140
