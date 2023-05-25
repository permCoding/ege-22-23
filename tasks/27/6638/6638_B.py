from math import ceil

f = open('./27B_6638.txt')
n = int(f.readline())
w = [0] * 10_000_000
for e in f:
    km, s = map(int, e.split())
    w[km] = ceil(s/100)

sma, sma_ = 0, 0
smb, smb_ = 0, 0
smb_ = sum(w[1:])
smb = sum(j*w[j] for j in range(1, len(w)))

mn = min(10**50, smb)
for i in range(1, len(w)):
    sma_ += w[i-1]
    sma += sma_
    smb -= smb_
    smb_ -= w[i]
    tmp = sma + smb
    if tmp < mn:
        mn = tmp
        pos = i

print(mn, pos)  # pos = 4992760

'''
a _ _ _ _ _
_ a _ _ _ _
_ _ a _ _ _

'''