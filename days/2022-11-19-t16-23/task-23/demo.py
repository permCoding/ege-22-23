def get(x, y):
    if x == 17: return 0
    if x > y: return 0
    if x == y: return 1
    return get(x+1, y) + get(x*2, y)


print(get(1, 10)*get(10, 35))

