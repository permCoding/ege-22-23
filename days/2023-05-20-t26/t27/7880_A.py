f = open('./7880_A.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

count = 0
for i in range(n):  # первое число
    for j in range(i+1, i+k+1):  # второе число
        if j < n:  # не должно выходить за правую границу
            if (t[i]+t[j])%17 == 0:
                count += 1
print(count)

# 15079
# 128655900
