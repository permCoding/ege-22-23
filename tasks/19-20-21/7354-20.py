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
        return all(t)
    else:
        return any(t)

a = []
for s in range(1, 31):  # Петя-Ваня-Петя
    if f(s,99) and not(f(s,1)):
        a.append(s)
print(a, len(a))

# [2, 4, 6, 8, 10, 12, 14] 7
