f = open('./6056.txt')
n = int(f.readline())
t = [int(e) for e in f]
t.sort(reverse=True)

k, a = 1, t[0]
for i in range(1, n):
    if a - t[i] >= 56:
        k += 1
        a = t[i]
print(k, a)  # 177 78

'''
сортируем первый столб
=ЕСЛИ(B1-A2>=56;A2;B1)
=ЕСЛИ(B1-B2>0;1;0)
=СУММ(C:C)
и последний не нулевой
'''