f = open("26_edj_01.txt")
s, n = map(int, f.readline().split())
lst = sorted([int(e) for e in f])
tmp = 0
for i in range(n):
    if tmp + lst[i] > s: break
    tmp += lst[i]
i -= 1
tmp -= lst[i]
r = 0
for j in range(i, n):
    if tmp + lst[j] > s:
        break
    else:
        last = lst[j]

print(tmp+last, n-j+1)
