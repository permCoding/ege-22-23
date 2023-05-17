f = open('./4660.txt')
n = int(f.readline())
t = [int(e) for e in f]

t.sort()

sm2 = sum(t) - sum(t[:n//4])//2 
print(sm2)  # 48825239 - второй ответ

sa = sum(t[i]//2 for i in range(0, n, 4))
print(sum(t) - sa)  # 44101521 - это первый ответ

sa, sb = 0, 0
for i in range(0, n, 4):
    sb += sum(t[i+1:i+4])
    sa += t[i]//2
print(sa+sb)  # 44101521 - это первый ответ
