f = open("26_2022_11.txt")  # 5228
n = int(f.readline())
lst = sorted([int(e) for e in f])[::-1]

res = [lst[0]]
for i in range(1, n):
    if res[-1] - lst[i] >= 8:
        res.append(lst[i])

print(len(res), res[-1])
