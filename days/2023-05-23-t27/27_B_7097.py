from math import ceil

f = open('./27_B_7097.txt')
n = int(f.readline())
t = [0] * 10_000_000
for e in f:
    km, p = map(int, e.split())
    t[km] = ceil(p/44)

# нулевое решение - когда лабор в пункте 0
# суммы доставок - sma, smb
sma_, sma = 0, 0
smb_, smb = sum(t[1:]), sum(i*t[i] for i in range(1, len(t)))

mn = smb  # вдруг 0-ая точка и есть лучшее решение
for i in range(1, len(t)):  # двигаем лабораторию
    sma_ += t[i-1]
    sma += sma_
    smb -= smb_
    smb_ -= t[i]
    if t[i] != 0:  # км где существ пункт приёма
        mn = min(mn, sma+smb)  # сумма доставок слева и справа
print(mn)  # _____

'''
0 1 2 3 4 5 6 <- i
a _ _ _ _ _ _
_ a _ _ _ _ _
_ _ a _ _ _ _
smd = sma + smb

0 1 2 3 4 5
_ a q w e r => q*1 + w*2 + e*3 + r*4
_ _ a w e r => _____ w*1 + e*2 + r*3
____________________ w + e + r
-t[i]


'''