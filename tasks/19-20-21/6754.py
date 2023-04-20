def f(s, step):
    if s>=351: return step%2 == 0
    if step == 0: return False
    
    step -= 1
    t = [
            f(s+1, step), 
            f(s+4, step), 
            f(s*2, step)
        ]
    if step%2 != 0:
        return all(t)  # при любом ходе противника
    else:
        return any(t)  # найдётся ход победителя

a = []
for s in range(1, 351):  # Петя1-Ваня1-Петя2-Ваня2-Петя3-Ваня3
    # if f(s,2):  # победа на первом ходу Вани
    # if f(s,3) and not(f(s,1)):  # победа Пети не на первом ходу
    if f(s,4) and not(f(s,2)):  # победа на первом ходу Вани
        a.append(s)
print(a)

# 19 - [175]
# 20 - [171, 174]
# 21 - [170, 173]
