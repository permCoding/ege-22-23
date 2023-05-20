f = open('./26_6031.txt')
n = int(f.readline())
t = sorted(map(int, f))[::-1]  # по убыванию

last, cnt = t[0], 1
for i in range(1, n):
    if last-t[i] >= 6:
        cnt += 1
        last = t[i]
print(cnt, last)  # 1575 50
