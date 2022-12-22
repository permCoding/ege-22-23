f = open("26_2022_09.txt")  # 4938
line = f.readline()
m, n = map(int, line.split())

lst = []
while True:
    line = f.readline()
    if not line: break
    a, b = map(int, line.split())
    lst.append((a,b))

srt = sorted(lst, key=lambda x: x[1])
pred, cnt = (0,0), 0
for elm in srt:
    if elm[0] >= pred[1]:
        pred = elm
        cnt += 1

print(cnt, pred)
