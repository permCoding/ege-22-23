def get(x, y):
    lst = [0] * 1000
    lst[x] = 1
    for i in range(x , y):
        if i != 17:
            lst[i+1] += lst[i]
            lst[i*2] += lst[i]
    return lst[y]


print(get(1, 10) * get(10, 35))
