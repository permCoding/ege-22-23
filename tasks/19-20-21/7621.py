def f19(n, step):
    if n >= 43: return step % 2 == 0  # выиграл ли победитель
    if step == 2: return False
    #if step == 2: return n >= 43  # выиграл ли Ваня
    #if step == 1 and n >= 43: return False  # нельзя чтобы выиграл Петя первым ходом

    step += 1
    a = f19(n+1, step)
    b = f19(n+4, step)
    c = f19(n*3, step)

    if step == 1:
        return a and b and c  # при любом ходе Пети
    else:
        return a or b or c  # Ваня может выиграть

for s in range(1, 43):
    if f19(s, 0):  # ход Пети
        print(s)
        break


def f20(n, step):
    if step == 3: return n >= 43  # выиграл ли Петя
    if step == 2 and n >= 43: return False  # нельзя чтобы выиграл Ваня первым ходом
    if step == 1 and n >= 43: return False  # нельзя чтобы выиграл Петя первым ходом

    step += 1
    a = f20(n+1, step)
    b = f20(n+4, step)
    c = f20(n*3, step)

    if step == 2:
        return a and b and c  # при любом ходе Вани
    else:
        return a or b or c  # Петя может выиграть

#for s in range(1, 43):  # Петя - Ваня - Петя
    #if f20(s, 0):  # ход Пети
        #print(s)


def f21(n, step):
    if step == 4 or step == 2: return n >= 43  # выиграл ли Ваня
    #if step == 2 and n >= 43: return False  # нельзя чтобы выиграл Ваня первым ходом
    if (step == 1 or step == 3) and n >= 43: return False  # нельзя чтобы выиграл Петя

    step += 1
    a = f21(n+1, step)
    b = f21(n+4, step)
    c = f21(n*3, step)

    if step == 1 or step == 3:
        return a and b and c  # при любом ходе Пети
    else:
        return a or b or c  # Ваня может выиграть

#for s in range(1, 43):  # Петя - Ваня - Петя
    #if f21(s, 0):  # ход Пети
        #print(s)
        #break

'''
№ 7621 Досрочная волна 2023 (Уровень: Базовый)

Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

Задание 20.
Для игры, описанной в задании 19, найдите два наименьших значения S,
при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.

Задание 19
Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежит куча камней.
Игроки ходят по очереди, первый ход делает Петя.
За один ход игрок может добавить в кучу один или четыре камня
либо увеличить количество камней в куче в три раза.
У каждого игрока есть неограниченное количество камней, чтобы делать ходы.

Игра завершается в тот момент,
когда количество камней в куче становится не менее 43.
Победителем считается игрок, сделавший последний ход,
т.е. первым получивший кучу из 43 камней или больше.

В начальный момент в куче было S камней; 1 ≤ S ≤ 42.

Будем говорить, что игрок имеет выигрышную стратегию,
если он может выиграть при любых ходах противника.

Укажите минимальное значение S, при котором
- Петя не может выиграть за один ход,
- но при любом ходе Пети Ваня может выиграть своим первым ходом.

'''