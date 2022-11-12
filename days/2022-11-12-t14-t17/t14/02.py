def to_int_(a, base):
    a = a[::-1]
    result = 0
    for p in range(len(a)):
        pos = alph.find(a[p])
        result += pos * base ** p
    return result


def to_int(a, base):
    result, p = 0, 0
    for smb in a[::-1]:
        pos = alph.find(smb)
        result += pos * base ** p
        p += 1
    return result


alph = '0123456789abcdef'
a = '10000'  # 'bab2'
print(to_int(a, 16))


# 203(10) = 2*10**2 + 0*10**1 + 3*10**0
# '1a'(16) = 1*16**1 + a*16**0
