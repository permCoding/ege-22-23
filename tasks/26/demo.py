f = [int(line) for line in open("demo.txt")]

n = f[0]
lst = sorted(f[1:], reverse=True)

res = [lst[0]]
for elm in lst[1:]:
    if res[-1] - elm >= 3:
        res.append(elm)

print(len(res), res[-1])
