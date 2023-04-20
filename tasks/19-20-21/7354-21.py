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
for s in range(1, 31):  # Петя1-Ваня1-Петя2-Ваня2-Петя3-Ваня3
    if f(s,6) and not(f(s,4)):
        a.append(s)
print(a, min(a))

# [7, 11] 7
