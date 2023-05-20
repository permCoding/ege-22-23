f = open('./26_7096.txt')
n = int(f.readline())
t = sorted([int(e) for e in f], reverse=True)

last, cnt = t[0], 1
for e in t:
    if last - e >= 11:
        cnt += 1
        last = e
print(cnt, last)
