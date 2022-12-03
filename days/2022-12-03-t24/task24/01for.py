# https://inf-ege.sdamgia.ru/problem?id=27686

s = open('01.txt').readline()
tmp, mx = 0, 0
for smb in s:
    if smb == 'X':
        tmp += 1
        mx = max(mx, tmp)
    else:
        tmp = 0
print(mx)

'''
Текстовый файл состоит не более чем из 10**6
символов X, Y и Z. Определите длину самой
длинной последовательности, состоящей из символов X.
Хотя бы один символ X находится в последовательности.

bed = 'YZ'
for smb in bed:
    s = s.replace(smb, ' ')

                if tmp > mx:
                    mx = tmp
'''
