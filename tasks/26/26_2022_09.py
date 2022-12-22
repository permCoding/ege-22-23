f = open("26_2022_09.txt")  # 4938
m, n = map(int, f.readline().split())

lst = []
for line in f:
    ss = line.split()
    lst.append((int(ss[0]),int(ss[1])))

lst.sort(key=lambda x: x[1])
res = [lst[0]]
i = 1
while i < n:
    if lst[i][0] >= res[-1][1]:
        res.append(lst[i])
    i += 1

print(len(res), res[-1])
