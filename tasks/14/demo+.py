# https://inf-ege.sdamgia.ru/problem?id=47218

for i in '0123456789ABCDE':
    a = '123' + i + '5'
    b = '1' + i + '233'
    r = int(a, 15) + int(b, 15)
    if r % 14 == 0:
        print(r // 14)
        break

# Операнды арифметического выражения записаны 
# в системе счисления с основанием 15:
# 123X5(15) + 1X233(15)
# Определите наименьшее значение x, при котором 
# значение данного арифметического выражения кратно 14. 
# Для найденного значения x вычислите частное от деления 
# значения арифметического выражения на 14 и 
# укажите его в ответе в десятичной СС
