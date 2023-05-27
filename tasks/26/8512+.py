f = open('./26_8512.txt')
k = int(f.readline())
n = int(f.readline())
t = [list(map(int, e.split())) for e in f]
t.sort()

cnt, cells = 0, [0] * (k+1)  # время до которого занята ячейка j
for e in t:  # n - все багажи 
    for j in range(1, k+1): # k - все ячейки камеры хр
        if e[0] > cells[j]:
            cells[j] = e[1]
            cnt += 1
            break  # как только нашли подходящ то всё
print(cnt, j)

'''
2
5
30 60
40 60
50 1110
61 1010
1100 1440
'''