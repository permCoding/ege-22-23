def f(s, step):
    if s<=12: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [f(s-12, step), f(s//3, step)]    
    if step%2 != 0:
        # return any(t)  # 19 - Ваня выиграл своим первым ходом после неудачного хода Пети
        return all(t)  # при любом ходе противника
    else:
        return any(t)  # найдётся ход победителя

a = []
for s in range(13, 300):  # Петя1-Ваня1-Петя2-Ваня2-Петя3-Ваня3
    # if f(s,2):  # победа на первом ходу Вани
    # if f(s,3) and not(f(s,1)):  # победа Пети не на первом ходу
    if f(s,4) and not(f(s,2)):  # победа на первом ходу Вани
        a.append(s)
print(a, len(a))

# 19 - 116
# 20 - 51, 152
# 21 - 24
