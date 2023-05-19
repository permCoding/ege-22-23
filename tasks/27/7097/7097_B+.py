f = open('./27_A_7097.txt')
n = int(f.readline())
t = [0] * 1_000  # 10_000_000 !!! !!! !!! !!! !!!
for _ in range(n):
    pos, k = map(int, f.readline().split())
    t[pos] = (k-1)//44+1
# t = [6,0,55,2]
sm_ = sum(t[1:])
sma, smb = 0, 0
for i in range(1, len(t)): smb += i*t[i]
print(0, sm_, sma, smb)

mn = smb
for i in range(1, len(t)):
# for i in range(1, 50):    
    sma += sma + t[i-1]
    smb -= sm_
    sm_ -= t[i]
    print(i, sm_, sma, smb)
    if t[i]!=0: mn = min(mn, sma+smb)

print(mn)
