# https://inf-ege.sdamgia.ru/problem?id=47228
# s = 'DACODAADOFADOFAA'
s = open('./t24_47228.txt').readline()

i, c, m = 0, 0, 0
while i < len(s)-1:
    # p = s[i:i+2]
    # if p=='CA' or p=='CO' or p=='DA' or p=='DO' or p=='FA' or p=='FO':
    if s[i] in 'CDF' and s[i+1] in 'AO':
        i += 2
        c += 1
        m = max(m, c)  # if c > m: m = c
    else:
        i += 1
        c = 0

print(m)

'''
CA CO
DA DO
FA FO
Текстовый файл состоит из символов A, C, D, F и O.
Определите максимальное количество идущих 
подряд пар символов вида: согласная + гласная
'''