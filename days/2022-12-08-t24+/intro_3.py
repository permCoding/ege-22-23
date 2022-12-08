s = 'ABCCAABCAACCABABB'

p, cnt = -1, 0
while s.find('AB', p+1) > -1:
    p = s.find('AB', p+1)
    cnt += 1
print(cnt)

p, cnt = -1, 0
while True:
    p = s.find('AB', p+1)
    if p == -1:
        break
    cnt += 1
print(cnt)
