f = open('./27_A_7627.txt')
k = int(f.readline())
n = int(f.readline())
t = list(map(int, f))
# k = 3
# n = 5
# t = [15,2,0,10,30]
sm = 0
for i in range(n):
    for j in range(n):
        if j-i>=k:
            sm = max(sm, t[i]+t[j])
print(sm)
