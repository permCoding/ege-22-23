def get(x, y, z):
    if x in z: return 0
    if x > y: return 0
    if x == y: return 1
    pos1 = x+1
    pos2 = 2*x
    pos3 = x+3
    way1 = get(pos1, y, z)
    way2 = get(pos2, y, z)
    way3 = get(pos3, y, z)
    return way1 + way2 + way3


print(get(3,16,[6,12]))

'''
https://inf-ege.sdamgia.ru/problem?id=16825
Исполнитель РазДваТри преобразует число на экране.
У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Прибавить 3
Первая команда увеличивает число на экране на 1, 
вторая умножает его на 2, третья увеличивает на 3.
Программа для исполнителя РазДваТри — это посл-сть команд.
Сколько существует программ, которые преобразуют 
исходное число 3 в число 16 и при этом траектория 
вычислений не содержит чисел 6 и 12?
Траектория вычислений — это последовательность результатов 
выполнения всех команд программы.
'''