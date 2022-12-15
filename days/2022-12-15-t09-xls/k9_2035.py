cnt = 0
for line in open('k9_2035.txt'):
    t = line.split('\t')
    if int(t[0]) + int(t[1]) + int(t[2]) != 180:
        cnt += 1
print(cnt)
