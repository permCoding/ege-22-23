# https://inf-ege.sdamgia.ru/problem?id=13418

def get(x, y):
    if x == 26: return 0
    if x > y: return 0
    if x == y: return 1
    return get(x+1, y) + get(2*x+1, y)
    

print(get(1,27))

