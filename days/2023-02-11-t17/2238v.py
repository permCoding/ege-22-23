t = [int(e) for e in open("2238.txt").readlines()]
avg = sum(t) / len(t)
k, sm = 0, 0
for i in range(len(t)-2):
    a,b,c = t[i],t[i+1],t[i+2]
    if int(a>avg)+int(b>avg)+int(c>avg) >= 2:
        k += 1
        sm = max(sm, a+b+c)
print(k, sm)

# хотя бы два из трёх элементов больше, чем среднее
