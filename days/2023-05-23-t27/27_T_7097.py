from math import ceil

f = open('./27_T_7097.txt')
n = int(f.readline())
t = [0] * 11
for e in f:
    km, p = map(int, e.split())
    # t[km] = p//96 + (0 if p%96==0 else 1)  # 1
    # t[km] = (p + 95)//96  # 2
    t[km] = ceil(p/96)  # 3
print(t)

mn = 10**50
for i in range(len(t)):
    if t[i] != 0:
        sm = 0
        for j in range(len(t)):
            sm += abs(j-i) * t[j]
        mn = min(mn, sm)
print(mn)
