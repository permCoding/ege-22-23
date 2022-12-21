f = open("26_2022_11.txt")
n = int(f.readline())
lst = sorted([int(e) for e in f], reverse=True)

res = [lst[0]]
i = 1
while i < n:
    if res[-1] - lst[i] >= 8:
        res.append(lst[i])
    i += 1

print(len(res), res[-1])
