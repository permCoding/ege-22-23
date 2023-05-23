from math import ceil

f = open('./27_A.txt')
n = int(f.readline())
t = [0] * 1000
for e in f:
    pos, k = map(int, e.split())
    t[pos] = ceil(k/48)

mn = 10**99
for i in range(len(t)):
    if t[i]!=0:
        sm = sum(abs(i-j)*t[j] for j in range(len(t)))
        mn = min(mn, sm)

print(mn)  # 44645
