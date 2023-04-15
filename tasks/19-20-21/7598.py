def f(n, step):
    if n >= 78: return step%2 == 0
    if step == 0: return False
    step -= 1
    a,b,c = f(n+1,step),f(n+4,step),f(n*4,step)
    if step%2 != 0:
        return a and b and c
    else:
        return a or b or c

for s in range(1, 77):
    if f(s, 2):
        print(s)  # 19
        break

for s in range(1, 77):
    if f(s, 3) and not(f(s, 1)):
        print(s)  # найти 2 минимальных - 15 18

for s in range(1, 77):
    if f(s, 4) and not(f(s, 2)):
        print(s)  # 14
        break
