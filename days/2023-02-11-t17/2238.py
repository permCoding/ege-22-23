t = [int(e) for e in open("2238.txt").readlines()]
avg = sum(t) / len(t)
k, sm = 0, 0
for i in range(len(t)-2):
    a,b,c = t[i],t[i+1],t[i+2]
    u1 = a>avg and b>avg
    u2 = b>avg and c>avg
    u3 = a>avg and c>avg
    if u1 or u2 or u3:
        k += 1
        sm = max(sm, a+b+c)
print(k, sm)

# хотя бы два из трёх элементов больше,
# чем среднее арифметическое
