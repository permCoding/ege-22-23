def to_int(a, base):
    result, p = 0, 0
    for smb in a[::-1]:
        pos = alph.find(smb)
        result += pos * base ** p
        p += 1
    return result


alph = '0123456789abcde'
for x in alph:
    a = to_int(f'123{x}5', 15)
    b = to_int(f'1{x}233', 15)
    r = a + b
    if r % 14 == 0:
        print(r//14)
        break
