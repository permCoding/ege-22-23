s = open('./24_8510.txt').readline()
w = 'NOP'
mx, k = 1, 1
for i in range(len(s)-1):
    if (s[i] in w) and (s[i+1] in w):
        mx = max(mx, k)
        k = 1
    else:
        k += 1
print(mx)
