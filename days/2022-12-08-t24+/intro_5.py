s = 'BABCCAABCAACCCCCCCCCCCCCCCCCABABB'

lst = []
b = False
tmp = ''
for i in range(len(s)):
    if s[i] == 'A':
        tmp += s[i]
        b = not b
        if b == False:
            lst += [tmp]
            tmp = ''
    else:
        if b == True:
            tmp += s[i]

for item in lst:
    if len(item) >= 10 and 'B' not in item:
        print(item)
