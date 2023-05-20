f = open('./26_6056.txt')
n = int(f.readline())
t = sorted([int(e) for e in f], reverse=True)

last, cnt = t[0], 1
for e in t:
    if last - e >= 56:
        cnt += 1
        last = e
print(cnt, last)
