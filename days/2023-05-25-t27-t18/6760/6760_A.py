from math import ceil

f = open('./27_A_6760.txt')
n = int(f.readline())
t = [0] * 1_000
for e in f:
    km, p = map(int, e.split())
    t[km] = ceil(p/48)

sm = 10**50
for i in range(len(t)):
    if t[i]!=0:
        tmp = sum(abs(j-i)*t[j] for j in range(len(t)))
        sm = min(sm, tmp)

print(sm)  # 44645
