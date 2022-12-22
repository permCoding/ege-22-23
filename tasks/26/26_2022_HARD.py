f = open("26_2022_HARD.txt")  # 5377
n, m = map(int, f.readline().split('\t'))

lst_full, lst_sneg = [], []
for i in range(n):
    line = f.readline()
    if i < m:
        a, b = map(int, line.split('\t'))
        lst_full.append(a)
        lst_sneg.append(b)
    else:
        lst_full.append(int(line))

cnt_m = len([e for e in lst_sneg if e%2==0])
cnt_w = len([e for e in lst_full if e%2!=0 and not(e in lst_sneg)])
print(cnt_m, cnt_w)
