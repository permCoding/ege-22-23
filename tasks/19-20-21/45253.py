# https://inf-ege.sdamgia.ru/problem?id=45253
# https://inf-ege.sdamgia.ru/problem?id=45254
# https://inf-ege.sdamgia.ru/problem?id=45255
# 2 камня со сменой условия
def f(a,b, step):
    if a+b >= 231: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = [
        f(a+1,b,step),
        f(a*2,b,step),
        f(a,b+1,step),
        f(a,b*2,step)
    ]
    if step%2 != 0:
        # return any(t)  # 19
        return all(t)
    else:
        return any(t)

r = []
for s in range(1, 214):
    # if f(17, s, 2):  # 19 => 54
    # if not(f(17, s, 1)) and f(17, s, 3):  # 20 => 98 106
    if not(f(17, s, 2)) and f(17, s, 4):  # 21 => 97
        r.append(s)
print(r)
