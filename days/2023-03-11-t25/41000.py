def m(n):
    t = [d for d in range(1, n//2+1) if n%d==0]
    return 0 if len(t)<2 else sum(t[-2:])

count, n = 0, 11_000_000
while count < 5:
    n += 1
    r = m(n)
    if 0<r<10_000:
        count += 1
        print(r)

"""
https://inf-ege.sdamgia.ru/problem?id=41000
Пусть M(N) — сумма двух наибольших различных натуральных делителей 
натурального числа N, не считая самого числа и единицы. 
Если у числа N меньше двух таких делителей, 
то M(N) считается равным 0.

Найдите 5 наименьших натуральных чисел, превышающих 11_000_000, 
для которых 0<M(N)<10_000. В ответе запишите найденные значения
M(N) в порядке возрастания соответствующих им чисел N.
"""