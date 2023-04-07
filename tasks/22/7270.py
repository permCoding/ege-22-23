mt = 0
lst = [
    [0,0,[0],0]
]
for row in open('7270.txt'):
    row = row.split('\t')
    i, t = int(row[0]), int(row[1])
    w = [lst[int(e)][3] for e in row[2].split(';')]
    r = t + max(w)
    lst.append([i,t,w,r])
    mt = max(mt, r)
print(mt)
