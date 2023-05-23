from math import ceil

f = open('./27_T_7097.txt')
n = int(f.readline())
t = [0] * 11
for e in f:
    pos, k = map(int, e.split())
    t[pos] = ceil(k/96)

sma_, sma = 0, 0
smb_, smb = sum(t[1:]), sum(i*t[i] for i in range(len(t)))

mn = smb
for i in range(1, len(t)):
    sma_ += t[i-1]
    sma += sma_
    smb -= smb_
    smb_ -= t[i]
    if t[i]!=0: mn = min(mn, sma+smb)

print(mn)  # 32
