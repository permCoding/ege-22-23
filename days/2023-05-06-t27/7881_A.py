f = open('./7881_A.txt')

n = int(f.readline())
k = int(f.readline())
t = [int(f.readline()) for _ in range(n)]

count = 0
for i in range(0, n-1):  # a
    for j in range(i+1, min(n,i+k+1)):  # b / min(n,i+k+1)
        a, b = t[i], t[j]
        if (abs(a-b)%100==0) and ((a%37==0) ^ (b%37==0)): count += 1
print(count)  # 73

"""
пример для k = 3
0 1 2 3 4 5 6 7
a b b b _ _ _ _
_ a b b b _ _ _

для файла B тоже работает, там столько чисел:
100000
25000
за 5 минут находит решение неоптимальный алгоритм
1146648
"""