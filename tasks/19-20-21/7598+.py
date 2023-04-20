def f(n, step):
    if n >= 78: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [f(n+1,step),f(n+4,step),f(n*4,step)]
    return all(t) if step%2 != 0 else any(t)

for s in range(1, 77):
    #if f(s, 2):  # 19
    #if f(s, 3) and not(f(s, 1)):  # 15 18
    if f(s, 4) and not(f(s, 2)):  # 14
        print(s)
