# https://inf-ege.sdamgia.ru/problem?id=27686

s = open('01.txt').readline()
s = s.replace('Y', ' ').replace('Z', ' ')
lst = s.split()
print(len(max(lst)))

'''
Текстовый файл состоит не более чем из 10**6
символов X, Y и Z. Определите длину самой
длинной последовательности, состоящей из символов X.
Хотя бы один символ X находится в последовательности.

bed = 'YZ'
for smb in bed:
    s = s.replace(smb, ' ')
'''
