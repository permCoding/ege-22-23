from math import ceil

f = open('./27_B_6760.txt')
n = int(f.readline())
t = [0] * 10_000_000
for e in f:
    km, p = map(int, e.split())
    t[km] = ceil(p/48)

# для нулевой точки
sma_, sma = 0, 0
smb_, smb = sum(t[1:]), sum(i*t[i] for i in range(1,len(t)))

sm = smb
for i in range(1, len(t)):
    sma_ += t[i-1]
    sma += sma_
    smb -= smb_
    smb_ -= t[i]
    if t[i]!=0: sm = min(sm, sma+smb)
    
print(sm)  # 5431081659239

'''
a _ _ _ _
_ a _ _ _
_ _ a _ _
_ _ _ a _
_ _ _ _ a

'''