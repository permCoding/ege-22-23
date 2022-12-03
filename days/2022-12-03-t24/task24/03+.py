# https://inf-ege.sdamgia.ru/problem?id=45258

s = open('03.txt').readline()
s = s.replace('AB', '#').replace('CB', '#')
m = 0
for cnt in range(1, 240):
    if '#'*cnt in s:
        m = cnt
print(m)
'''
Текстовый файл состоит из символов A, B и C.
Определите максимальное количество идущих подряд 
пар символов AB или CB в прилагаемом файле.
'''