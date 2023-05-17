f = open('./6759.txt')
n = int(f.readline())
t = [int(e) for e in f]

t.sort(reverse=True)
k3 = n//3
sm3 = sum(t[:k3])
sma = sum(t) - sm3
print(sma)  # 22262050 - это первый ответ

smb = 0
for i in range(n):
    if (i+1)%3 != 0:
        smb += t[i]
print(smb)  # 33246829 - это второй ответ

