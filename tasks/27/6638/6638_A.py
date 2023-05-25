from math import ceil

f = open('./27A_6638.txt')
n = int(f.readline())
w = [0] * 1000
for e in f:
    km, s = map(int, e.split())
    w[km] = ceil(s/100)

pos, mn = 0, 10**50
for i in range(len(w)):
    sm = 0
    for j in range(len(w)):
        sm += abs(i-j)*w[j]
    if sm < mn:
        mn = sm
        pos = i
print(mn, pos)  # pos = 499
