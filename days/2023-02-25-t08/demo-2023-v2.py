k = 0
alp = '01234567'
for a in alp[1:]:
    for b in alp:
        for c in alp:
            for d in alp:
                for e in alp:
                    elm = a+b+c+d+e
                    if elm.count('6') == 1:
                        pos = elm.find('6')
                        if pos<4 and elm[pos+1] in '1357': continue
                        if pos>0 and elm[pos-1] in '1357': continue
                        k += 1
print(k)

"""
Определите количество пятизначных чисел,
записанных в восьмеричной системе счисления,
в записи которых только одна цифра 6,
при этом никакая нечётная цифра
не стоит рядом с цифрой 6.
"""
