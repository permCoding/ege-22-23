# https://inf-ege.sdamgia.ru/problem?id=27421

s = open('02.txt').readline()
t, m = 1, 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        t += 1
        m = max(m, t)
    else:
        t = 1
print(m)

'''
Текстовый файл состоит не более чем из 10**6
символов X, Y и Z.
Определите максимальное количество идущих подряд символов,
среди которых каждые два соседних различны.
'''
