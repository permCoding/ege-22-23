# https://inf-ege.sdamgia.ru/problem?id=27697
# s = 'LLDDDLD'
s = open('t24_27697.txt').readline()

m, c = 0, 0
for smb in s:
    if smb == 'D':
        c += 1
        m = max(m, c)
    else:
        c = 0

print(m)
