cnt = 0
for line in open('k9_2035.txt'):
    a,b,c = [int(e) for e in line.split('\t')]
    if a+b+c != 180: cnt += 1
print(cnt)
