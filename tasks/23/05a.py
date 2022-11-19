def get(x, y):
    lst = [0] * 100
    lst[x] = 1
    for i in range(x, y):
        if i != 12:
            lst[i+1] += lst[i]
            lst[i+2] += lst[i]
            lst[i*3] += lst[i]
    return lst[y]


print(get(2,9) * get(9,19))

'''
https://inf-ege.sdamgia.ru/problem?id=37158

'''