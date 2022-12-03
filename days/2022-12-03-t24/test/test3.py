def get_max(s, sep=' '):
    lst = s.split(sep)
    mx = 0
    for elm in lst:
        if int(elm) > mx:
            mx = int(elm)
    return mx


def get_max_gen(s, sep=' '):
    lst = s.split(sep)
    res = [int(elm) for elm in lst]
    return max(res)


s = '121 99 1009797 333'
print(get_max_gen(s))
