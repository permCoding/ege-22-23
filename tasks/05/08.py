# https://inf-ege.sdamgia.ru/problem?id=11235

for n in range(1000, 10000):
    lst = list(str(n))
    d = list(map(lambda x: int(x), lst))
    a,b,c = d[0]+d[1], d[1]+d[2], d[2]+d[3]
    lst = sorted([a,b,c])
    r = str(lst[1]) + str(lst[2])
    if r == '1418':
        print(n)
        break

'''
Автомат получает на вход четырёхзначное число. 
По этому числу строится новое число по следующим правилам.
1. Складываются отдельно первая и вторая цифры, 
   вторая и третья цифры, а также третья и четвёртая цифры.
2. Из полученных трёх чисел выбираются два наибольших и записываются 
   друг за другом в порядке неубывания без разделителей.
Пример. Исходное число: 9575. Суммы: 9 + 5 = 14; 5 + 7 = 12; 7 + 5 = 12. 
Наибольшие суммы: 14, 12. Результат: 1214.
Укажите наименьшее число, при обработке которого автомат выдаёт результат 1418.
'''
