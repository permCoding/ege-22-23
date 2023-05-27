s = open('./24_8510.txt').readline()

ln, w = 1, 'NOP'
lnm = 1
for i in range(len(s)-1):
    a, b = s[i], s[i+1]
    if (a in w) and (b in w):
        lnm = max(lnm, ln)
        ln = 1
    else:
        ln += 1
print(lnm)  # 57
