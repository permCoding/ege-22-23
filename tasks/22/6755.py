mt = 0
lst = [
    [0,0,[0],0]
]
for line in open('./6755.txt'):
    row = line.split('\t')
    i, t = int(row[0]), int(row[1])
    w = row[2].split(';')
    w = [int(e) for e in w]
    w = [lst[e][3] for e in w]
    r = t+max(w)
    lst.append([i,t,w,r])
    mt = max(mt, r)
print(mt)