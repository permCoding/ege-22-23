f = open('./27_T_7097.txt')
n = int(f.readline())
t = [0] * 11
for _ in range(n):
    pos, k = map(int, f.readline().split())
    t[pos] = (k-1)//96+1
print(t)

mn = 10**12
for i in range(len(t)):
    if t[i]!=0:  # только для существующих точек
        tmp = 0
        for j in range(len(t)):
            tmp += abs(i-j)*t[j]
        mn = min(mn, tmp)
print(mn)  # 32
