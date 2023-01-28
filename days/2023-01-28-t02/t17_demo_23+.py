lines = open("17.txt").read().split('\n')[:-1]
m = max([int(line) for line in lines if line[-1]=='3'])

k, sm = 0, 0
for i in range(len(lines)-1):
    a, b = lines[i], lines[i+1]
    if int(a[-1]=='3') ^ int(b[-1]=='3'):
        q = int(a)**2 + int(b)**2
        if q >= m**2:
            k += 1
            sm = max(sm, q)
print(k, sm)

# 1 число оканч на 3
# a**2+b**2 >= m**3
# m = макс эл-нт посл оканч на 3 = 9973
# 180 
