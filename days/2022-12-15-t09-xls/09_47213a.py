count = 0
f = open('09_47213.txt')
for s in f:
    arr = list(map(int, s.split(';')))
    rep = sum(arr) - sum(set(arr))
    mean_unrep = sum(set(arr) - {rep}) / 4
    if len(set(arr)) == 5 and mean_unrep <= 2 * rep:
        count += 1
print(count)
