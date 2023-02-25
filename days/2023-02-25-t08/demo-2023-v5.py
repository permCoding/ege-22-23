from itertools import product as p

k = 0
for elm in p('01234567', repeat=5):
    if elm.count('6') == 1 and elm[0] > '0':
        pos = elm.index('6')
        if (pos==4) or (pos<4 and elm[pos+1] in '024'):
            if (pos==0) or (pos>0 and elm[pos-1] in '024'):
                k += 1
print(k)

"""
Определите количество пятизначных чисел,
записанных в восьмеричной системе счисления,
в записи которых только одна цифра 6,
при этом никакая нечётная цифра
не стоит рядом с цифрой 6.
"""
