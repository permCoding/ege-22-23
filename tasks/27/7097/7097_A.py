f = open('./27_A_7097.txt')
n = int(f.readline())
t = [0] * 1000
for _ in range(n):
    pos, k = map(int, f.readline().split())
    t[pos] = (k-1)//44+1

mn = 10**28
for i in range(len(t)):
    if t[i]!=0:
        tmp = 0
        for j in range(len(t)):
            tmp += abs(i-j)*t[j]
        mn = min(mn, tmp)
print(mn)  # 55261
