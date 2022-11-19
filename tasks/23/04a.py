def get(x, y):
    lst = [0] * 1000
    lst[x] = 1
    for i in range(x, y):
        pos1 = i+1
        pos2 = i+2
        pos3 = i*2
        lst[pos1] += lst[i]
        lst[pos2] += lst[i]
        lst[pos3] += lst[i]
    return lst[y]


print(get(3,10) * get(10,12))

'''
https://inf-ege.sdamgia.ru/problem?id=11358

'''