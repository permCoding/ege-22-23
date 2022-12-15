cnt = 0
for line in open('09_47213.txt'):
    lst = [int(e) for e in line.split(';')]
    st = set(lst)
    a = len(st) == 5
    x = sum(lst) - sum(st)
    sa = (sum(st) - x) / 4
    b = sa <= 2*x
    if a and b: cnt += 1
print(cnt)

