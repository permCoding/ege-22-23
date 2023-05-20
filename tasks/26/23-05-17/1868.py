f = open('./1868.txt')
n = int(f.readline())
t = [list(map(int, e.split())) for e in f]

t.sort(key=lambda e: (-e[0],+e[1]))

for i in range(n-1):
    if t[i][0] == t[i+1][0]:
        if t[i+1][1]-t[i][1] == 3:
            print(t[i][0], t[i][1]+1)  # 8631 7311
            break
