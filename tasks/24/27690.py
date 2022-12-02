# https://inf-ege.sdamgia.ru/problem?id=27690
def solver1(s):
    t, m = 1, 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            t += 1
            m = max(m, t)
        else:
            t = 1
    print(m)


s = open("24_27690.txt").readline().strip()
solver1(s)
'''
Текстовый файл состоит не более чем из 10**6 символов A, B и C. 
Определите максимальное количество идущих подряд символов, 
среди которых каждые два соседних различны.
'''