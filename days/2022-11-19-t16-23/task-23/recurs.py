def get_sum1(lg, rg):
    if lg == rg:  # точка останова
        return rg
    else:
        return lg + get_sum1(lg+1, rg)  # шаг рекурсии


def get_sum2(lg, rg):
    if lg == rg: return rg
    return lg + get_sum2(lg+1, rg)


def get_sum3(lg, rg):
    if lg == rg: return rg
    return get_sum2(lg, rg-1) + rg


print(get_sum1(2, 5))
print(get_sum2(2, 5))
print(get_sum3(2, 5))
