t = list(map(int, open("6024.txt").readlines()))
m = max([e for e in t if e%100==12])
k, sm = 0, 0
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if (a+b)**2 < m**2:
        k += 1
        # sm
print(k)
