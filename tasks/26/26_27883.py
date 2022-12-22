# https://inf-ege.sdamgia.ru/problem?id=27883
f = open("26_27883.txt")  # и 27884
m, n = map(int, f.readline().split())
# t = sorted([int(line) for line in f])
t = sorted(map(int, f.readlines()))
r = []
for i in range(n):
    if sum(r) + t[i] > m: break
    r += [t[i]]
last = r.pop()
dif = m - sum(r)
for i in range(n-1, -1, -1):
    if t[i] <= dif:
        r += [t[i]]
        break
print(len(r), r[-1])
