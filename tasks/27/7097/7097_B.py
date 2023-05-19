f = open('./27_B_7097.txt')
n = int(f.readline())
t = [0] * 10_000_000  # 10_000_000 !!! !!! !!! !!! !!!
for _ in range(n):
    pos, k = map(int, f.readline().split())
    t[pos] = (k-1)//44+1

sm_ = sum(t[1:])
sma, smb = 0, 0
for i in range(1, len(t)): smb += i*t[i]
print(sm_, sma, smb)

mn = smb
for i in range(1, len(t)):
    if t[i]!=0:
        sma = 0
        for j in range(0, i): sma += (i-j)*t[j]
        smb = 0
        for j in range(i+1, len(t)): smb += (j-i)*t[j]
        mn = min(mn, sma+smb)

print(mn)
