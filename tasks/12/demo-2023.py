k = 0
s = '7' * 256
while '7777' in s or '1111' in s:
    if '7777' in s:
        s = s.replace('7777', '1', 1)
        k += 4
    else:
        s = s.replace('1111', '7', 1)
print(s, k)
