# https://inf-ege.sdamgia.ru/problem?id=40999

s = open('04.txt').readline()
lst = s.split('E')
m = 0
for elm in lst:
    if elm.count('A') >= 3:
        m = max(m, len(elm))
print(m)

'''
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z). 
Определите максимальное количество идущих подряд символов, 
среди которых нет ни одной буквы E и при этом не менее трёх букв A.
['', 'AA', '', '----', 'TTAAAT', 'VVVVVVVVVVVVVVVVVVVV']
'''