def get(x, y):
    if x == 12: return 0
    if x > y: return 0
    if x == y: return 1
    pos1 = x+1
    pos2 = x+2
    pos3 = x*3
    way1 = get(pos1, y)
    way2 = get(pos2, y)
    way3 = get(pos3, y)
    return way1 + way2 + way3


print(get(2,9) * get(9,19))

'''
https://inf-ege.sdamgia.ru/problem?id=37158

'''