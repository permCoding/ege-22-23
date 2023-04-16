def f(a,b, step):
    if a>=479 or b>=479: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [
            f(a+1,b,step), f(a+3,b,step), f(a*2,b,step),
            f(a,b+1, step), f(a,b+3,step), f(a,b*2,step)
        ]
    if step%2 != 0:
        return all(t)  # при любом ходе противника
    else:
        return any(t)  # найдётся ход победителя

a = []
for s in range(1, 479):  # Петя1-Ваня1-Петя2-Ваня2-Петя3-Ваня3
    # if f(239,s,2):  # победа на первом ходу Вани
    # if not(f(239,s,1)) and f(239,s,3):  # 
    if not(f(239,s,2)) and f(239,s,4):  # 
        a.append(s)
print(a, len(a))

# 19 - 239
# 20 - 236 238
# 21 - 235
