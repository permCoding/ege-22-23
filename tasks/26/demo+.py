f = [int(line) for line in open("demo.txt")]

lst = sorted(f[1:], reverse=True)

pred = lst[0]
cnt = 1
for elm in lst[1:]:
    if pred - elm >= 3:
        cnt += 1
        pred = elm

print(cnt, pred)
