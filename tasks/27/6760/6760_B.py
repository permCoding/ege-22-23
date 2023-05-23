from math import ceil

f = open('./27_B.txt')
n = int(f.readline())
t = [0] * 10_000_000
for e in f:
    pos, k = map(int, e.split())
    t[pos] = ceil(k/48)

sma_, sma = 0, 0
smb_, smb = sum(t[1:]), 0
for i in range(1, len(t)): smb += i*t[i]

mn = smb
for i in range(1, len(t)):
    sma_ += t[i-1]
    sma += sma_
    smb -= smb_
    smb_ -= t[i]
    if t[i]!=0: mn = min(mn, sma+smb)

print(mn)  # 5431081659239
