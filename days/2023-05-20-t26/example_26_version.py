f = open('./example_26_normal.txt')
n = int(f.readline())
t = [list(map(int, e.split())) for e in f]
t.sort()

for i in range(n-1, 0, -1):
    a, b = t[i], t[i-1]
    if a[0] == b[0]:
        if a[1]-b[1] == 3+1:
            print(b[0], b[1]+1)
            break
