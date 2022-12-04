# https://inf-ege.sdamgia.ru/problem?id=27421

s = open('02.txt').readline().strip()

s = s \
    .replace('XX', 'X X') \
    .replace('YY', 'Y Y') \
    .replace('ZZ', 'Z Z')

lst = s.split()
print(lst)
print(len(max(lst, key=len)))
print(max([len(elm) for elm in lst]))

'''
Текстовый файл состоит не более чем из 10**6
символов X, Y и Z.
Определите максимальное количество идущих подряд символов,
среди которых каждые два соседних различны.
'''
