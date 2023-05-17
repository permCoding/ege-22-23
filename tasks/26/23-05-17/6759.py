f = open('./6759.txt')
n = int(f.readline())
t = [int(e) for e in f]

t.sort(reverse=True)

sma = sum(t) - sum(t[:n//3])
print(sma)  # 22262050 - это первый ответ

print(sum(t) - sum(t[-n//3:]))
print(sum(t) - sum(t[::-1][:n//3]))

smb = 0
for i in range(n):
    if (i+1)%3 != 0:
        smb += t[i]
print(smb)  # 33246829 - это второй ответ

