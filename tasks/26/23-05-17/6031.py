f = open('./6031.txt')
n = int(f.readline())
t = [int(e) for e in f]
t.sort(reverse=True)

k, a = 1, t[0]
for i in range(1, n):
    if a - t[i] >= 6:
        k += 1
        a = t[i]
print(k, a)  # 1575 50
