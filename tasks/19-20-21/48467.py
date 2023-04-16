# https://inf-ege.sdamgia.ru/problem?id=48467
# https://inf-ege.sdamgia.ru/problem?id=48468
# https://inf-ege.sdamgia.ru/problem?id=48469
# 2 камня, но на сайте ответ с ошибкой
def f(s, step):
    if s >= 151: return step%2 == 0
    if step == 0: return False
    step -= 1
    t = []
    if (s+1)%3 != 0: t.append(f(s+1, step))
    if (s+2)%3 != 0: t.append(f(s+2, step))
    if (s*2)%3 != 0: t.append(f(s*2, step))
    if step%2 != 0:
        return all(t)
    else:
        return any(t)

r = []
for s in range(1, 150):
    # if f(s, 2):  # 19 => 74
    # if not(f(s,1)) and f(s, 3):  # 37 72 73
    # на сайте пишут что 72 нельзя так как делится на 3
    # но ведь нельзя "делать ход, после которого количество камней в куче будет делиться на 3."
    # а вот ходить ИЗ кучки камней где их кол-во дел на 3 не запрещено
    if not(f(s,2)) and f(s, 4):  # 71
        r.append(s)
print(r)