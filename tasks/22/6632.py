mt = 0
lst = [
    [0,0,0]
]
for line in open('./6632.txt'):
    row = line.split('\t')
    i,t = int(row[0]), int(row[1])
    w = map(int, row[2].split(';'))
    w = [lst[e][2] for e in w]
    r = t + max(w)
    lst.append([i,t,r])
    mt = max(mt,r)
print(mt)