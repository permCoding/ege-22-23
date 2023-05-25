from math import ceil

f = open('./27_A_7097.txt')
n = int(f.readline())
t = [0] * 1_000
for e in f:
    km, p = map(int, e.split())
    t[km] = ceil(p/44)

mn = 10**50
for i in range(len(t)):
    if t[i] != 0:  # км где существ пункт приёма
        sm = sum(abs(j-i) * t[j] for j in range(len(t)))
        mn = min(mn, sm)
print(mn)  # 55261
