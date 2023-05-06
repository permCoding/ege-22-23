f = open('test_A.txt')

n, m = map(int, f.readline().split())
t = [int(f.readline()) for _ in range(n)]
mx = 0
for i in range(n-m):
    for j in range(i+m, n):
        if t[i]+t[j] > mx:
            mx = t[i]+t[j]
print(mx)