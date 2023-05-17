f = open('./4684.txt')
n = int(f.readline())
t = [int(e) for e in f]

t.sort()

sm2 = sum(t) - sum(t[:n//6])//2 
print(sm2)  # 49699604 - второй ответ

t.sort(reverse=True)
sa = sum(t[i]//2 for i in range(5, n, 6))
print(sum(t) - sa)  # 46201709 - это первый ответ

sa, sb = 0, 0
for i in range(0, n, 6):
    if n-i>=6:
        sb += sum(t[i:i+5])
        sa += t[i+5]//2
    else:
        sb += sum(t[i:])
print(sa+sb)  # 44101521 - это первый ответ
