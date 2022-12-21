f = open("26_2022_09.txt")
m, n = map(int, f.readline().split())

lst = []
for line in f:
    a, b = map(int, line.split())
    lst.append((a,b))

lst.sort(key=lambda x: x[1])
res = [lst[0]]
i = 1
while i < n:
    if lst[i][0] >= res[-1][1]:
        res.append(lst[i])
    i += 1

print(len(res), res[-1])
