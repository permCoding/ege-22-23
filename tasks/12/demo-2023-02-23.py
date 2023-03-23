n = 34
s = '1'*n + '2'*n
while '12' in s or '21' in s:
    if '12' in s:
        s = s.replace('12', '21', 1)
    else:
        s = s.replace('21', '111', 1)
print(s, s.count('1'), 2*n)
