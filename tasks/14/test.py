def func0():
    for x in range(10):
        a = int(f'123{x}5', 15)
        b = int(f'1{x}233', 15)
        r = a + b
        if r % 14 == 0:
            print(r // 14)
            break


def func1():
    x = 0
    while x < 10:
        a = '123' + str(x) + '5'
        b = '1' + str(x) + '233'
        a = int(a, 15)
        b = int(b, 15)

        r = a + b

        if r % 14 == 0:
            print(r // 14)
            break
        x += 1


def func2():
    s = '0123456789abcdef'

    def to_int(n, base):
        res, p = 0, 0
        for smb in n[::-1]:
            pos = s.find(smb)
            res += pos * base**p
            p += 1
        return res

    for x in s:
        a = '123' + str(x) + '5'
        b = '1' + str(x) + '233'
        a = to_int(a, 15)
        b = to_int(b, 15)

        r = a + b

        if r % 14 == 0:
            print(r // 14)
            break


def func3():
    s = '0123456789abcdef'

    def to_int_rec(n, base, p):
        if n == '':
            return 0
        smb = n[-1]
        pos = s.find(smb)
        return pos * base**p + to_int_rec(n[:-1], base, p+1)

    for x in s:
        a = to_int_rec(f'123{x}5', 15, 0)
        b = to_int_rec(f'1{x}233', 15, 0)
        r = a + b
        if r % 14 == 0:
            print(r // 14)
            break


func0()
func1()
func2()
func3()

# s = '0123456789abcdef'
#
#
# def to_int(n, base):
#     res, p = 0, 0
#     for smb in n[::-1]:
#         pos = s.find(smb)
#         res += pos * base**p
#         p += 1
#     return res
#
#
# e = '123'
# print(int(e, 15))
# print(to_int(e, 15))
