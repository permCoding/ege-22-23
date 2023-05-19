f = open('27_A_7275.txt')
n, m = map(int, f.readline().split())
t = [0] * 1_000 # A

for _ in range(n):
    line = f.readline()
    pair = line.split()
    a, b = int(pair[0]), int(pair[1])
    b = (b-1)//30+1
    t[a] = b

mx = 0
for i in range(m, len(t)-m):
    if t[i]!=0:
        mx = max(mx, sum(t[i-m:i+m+1]))
print(mx)  # 264

#for e in t[:10]:
    #print(e)

#01 = 1 0
#29 = 1 0
#30 = 1 1

#31 = 2 1
#58 = 2 1
#59 = 2 1
#60 = 2 2
