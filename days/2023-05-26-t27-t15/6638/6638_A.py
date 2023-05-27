from math import ceil

f = open('./27A_6638.txt')
n = int(f.readline())
t = [0] * 1000
for e in f:
    km, sign = map(int, e.split())
    t[km] = ceil(sign/100)

pos, mn = 0, 10**99
for i in range(len(t)):
    sm = 0
    for j in range(len(t)):
        sm += abs(j-i)*t[j]
    if sm < mn:
        mn = sm
        pos = i
print(mn, pos)
