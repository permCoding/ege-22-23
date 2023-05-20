f = open('./7096.txt')
n = int(f.readline())
t = [int(e) for e in f]
t.sort(reverse=True)

k, a = 1, t[0]
for i in range(1, n):
    if a - t[i] >= 11:
        k += 1
        a = t[i]
print(k, a)  # 854 54

'''
sort rev
=ЕСЛИ(B1-A2>=11;A2;B1)
=ЕСЛИ(B1<>B2;1;0)
=СУММ(C:C)
last
'''
