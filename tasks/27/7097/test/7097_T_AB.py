from math import ceil

f = open('./27_T_7097.txt')
n = int(f.readline())
t = [0] * 11
for e in f:
    pos, k = map(int, e.split())
    t[pos] = ceil(k/96)

mn = 10**99
for i in range(len(t)):
    if t[i]!=0:
        sma = sum((i-j)*t[j] for j in range(0, i))
        smb = sum((j-i)*t[j] for j in range(i+1, len(t)))
        mn = min(mn, sma+smb)

print(mn)  # 32
