def f(s, step):
    if s>=31: return step%2 == 0
    if step == 0: return False
    
    step -= 1
    t = [
            f(s+1, step), 
            f(s+5, step), 
            f(s*2, step)
        ]
    if step%2 != 0:
        return any(t)  # 19
    else:
        return any(t)

for s in range(1, 31):
    if f(s,3):  # Петя-Ваня-Петя
        print(s)
        break

# 3
