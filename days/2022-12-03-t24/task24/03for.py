# https://inf-ege.sdamgia.ru/problem?id=45258

s = open('03.txt').readline()
t, m = 0, 0
i = 0
while i < len(s)-1:
    # if s[i]+s[i+1] == 'AB' or s[i]+s[i+1] == 'CB':
    # if s[i]+s[i+1] in ['AB','CB']:
    if s[i:i+2] in ['AB','CB']:
        t += 1
        m = max(m, t)
        i += 2
    else:
        t = 0
        i += 1
print(m)

'''
Текстовый файл состоит из символов A, B и C.
Определите максимальное количество идущих подряд 
пар символов AB или CB в прилагаемом файле.
'''