s = open("24.txt").readline() + 'W'

lst = ['FA','FO','CA','CO','DA','DO']

max_d, d = 0, 0
i = 0
while i < len(s) - 1:
    if s[i]+s[i+1] in lst:
        d += 1
        i += 2
    else:
        d = 0
        i += 1
    max_d = max(max_d, d)
        
print(max_d)
