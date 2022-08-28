f = [int(line) for line in open("26.txt")]

n = f[0]
lst = sorted(f[1:], reverse=True)

res = [lst[0]]
for i in range(1, n):
    if res[-1] - lst[i] >= 3:
        res.append(lst[i])

print(len(res), sep="", end="; ")
print(res[-1])
