# https://inf-ege.sdamgia.ru/problem?id=27695

s = open('t24_27695.txt').readline()

c, m = 1, 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        c += 1
        m = max(m, c)
    else:
        c = 1

print(m)
