f = open('./7880_A.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

count = 0
for i in range(0, n-1):  # первое число
    for j in range(i+1, i+1+k):  # второе число на расстоянии не более чем
        if j < n:  # не должно вых за пред длины списка чисел
            if (t[i]+t[j])%17 == 0: 
                count += 1
print(count)  # 15079
