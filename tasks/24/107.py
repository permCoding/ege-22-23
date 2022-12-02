# https://inf-ege.sdamgia.ru/problem?id=45258
def solver0(s):
    s = s.replace('AB', 'CB')
    m = 0
    for i in range(1, 200):
        if 'CB'*i in s:
            m = i
    print(m)

def solver1(s):
    s = s.replace('AB', '#').replace('CB', '#')
    s = s.replace('A',' ').replace('B',' ').replace('C',' ')
    print(max([len(x) for x in s.split()]))

def solver2(s):
    p, m = 0, 0
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] in ['AB', 'CB']:
            p += 1
            m = max(p, m)
            i += 2
        else:
            p = 0
            i += 1
    print(m)


solver0(open("./107.txt").readline().strip())

'''
из A B C
Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB, 
или только из пар AB и CB в произвольном порядке следования этих пар.

CBAAAABABCBAAABCBBABCB
#AAA###AA##B######BA#C
#   ###  ## ######  # 
'''