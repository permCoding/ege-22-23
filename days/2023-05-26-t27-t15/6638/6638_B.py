from math import ceil

f = open('./27B_6638.txt')
n = int(f.readline())
t = [0] * 10_000_000
for e in f:
    km, sign = map(int, e.split())
    t[km] = ceil(sign/100)

sma_, sma = 0, 0
smb_, smb = sum(t[1:]), sum(j*t[j] for j in range(1, len(t)))

pos, mn = 0, 10**99
for i in range(1, len(t)):
    sma_ += t[i-1]
    sma += sma_
    smb -= smb_
    smb_ -= t[i]
    if sma+smb < mn and t[i]!=0:  # только для тех точек где есть антенна
        mn = sma + smb
        pos = i
print(mn, pos)
'''
0 1 2 3 4 5 6
a _ _ _ _ _ _
_ a _ _ _ _ _
_ _ a _ _ _ _

'''