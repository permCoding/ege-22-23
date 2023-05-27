f = open('./26_8512.txt')
k = int(f.readline())
n = int(f.readline())
t = [list(map(int, e.split())) for e in f]
t.sort()

cells = [0] * k  # время до которого занята ячейка j
cnt = 0
for i in range(n):  # n - все багажи 
    for j in range(k): # k - все ячейки камеры хр
        if t[i][0] > cells[j]:
            cells[j] = t[i][1]
            cnt += 1
            break  # как только нашли подходящ то всё
print(cnt, j+1)

'''
2
5
30 60
40 60
50 1110
61 1010
1100 1440
'''