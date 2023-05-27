f = open('./27_A_8513.txt')
k = int(f.readline())
n = int(f.readline())
t = list(map(int, f))
sm = 0
for i in range(n):
    for j in range(n):
        if j-i>=k:
            sm = max(sm, t[i]+t[j])
print(sm)  # 1219
