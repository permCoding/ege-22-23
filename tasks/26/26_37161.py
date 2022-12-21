f = open("26_37161.txt")
n = int(f.readline())
t = [tuple(map(int, line.split())) for line in f]

t = sorted(t, key=lambda x: (-x[0], x[1]))

for i in range(n-1):
    a, b = t[i], t[i+1]
    if a[0] == b[0] and b[1]-a[1] == 3:
        print(a)
