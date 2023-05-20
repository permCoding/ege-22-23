f = open('./example_26.txt')
n = int(f.readline())
t = []
for i in range(n):
    line = f.readline()
    r, c = line.split()
    t.append( [int(r), int(c)] )
# t.sort()
t.sort(key=lambda e: (-e[0],+e[1]))

for i in range(n-1):
    if t[i][0] == t[i+1][0]:
        if t[i+1][1]-t[i][1] == 3+1:
            print(t[i][0], t[i][1]+1)
            break
