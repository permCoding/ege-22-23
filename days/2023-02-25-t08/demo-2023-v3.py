start, finish = '10000', '77777'
a, b = int(start, 8), int(finish, 8)

k = 0
for dec in range(a, b+1):
    elm = oct(dec)[2:]
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

int - The allowed values are 0 and 2–36.

"""
