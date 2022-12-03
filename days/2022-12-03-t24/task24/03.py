# https://inf-ege.sdamgia.ru/problem?id=45258

s = open('03.txt').readline()
s = s \
    .replace('AB', '#') \
    .replace('CB', '#') \
    .replace('A', ' ') \
    .replace('B', ' ') \
    .replace('C', ' ')
lst = s.split()
print(len(max(lst)))

'''
Текстовый файл состоит из символов A, B и C.
Определите максимальное количество идущих подряд 
пар символов AB или CB в прилагаемом файле.
'''