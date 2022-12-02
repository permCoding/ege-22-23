# https://inf-ege.sdamgia.ru/problem?id=27686

def solver1(s):
    s = s.replace('Y', ' ').replace('Z', ' ')
    print(max([len(x) for x in s.split()]))

def solver2(s):
    t, m = 0, 0
    for i in range(len(s)):
        if s[i] == 'X':
            t += 1
            m = max(t, m)
        else:
            t = 0
    print(m)

solver2(open("24_27686.txt").readline().strip())
'''
Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. 
Определите длину самой длинной последовательности, состоящей из символов X. 
Хотя бы один символ X находится в последовательности.
'''