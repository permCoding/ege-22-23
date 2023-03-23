import re

for num in range(2023, 10**10 + 1, 2023):
    ptn = '^1.2139.*4$'
    if re.match(ptn, str(num)):
        print(num, num//2023)

"""
Среди натуральных чисел, не превышающих 10**10, найдите все числа,
соответствующие маске 1?2139*4, делящиеся на 2023 без остатка.
В ответе запишите в первом столбце таблицы все найденные числа
в порядке возрастания, а во втором столбце – соответствующие им
результаты деления этих чисел на 2023.
"""