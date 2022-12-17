f = open("2091.txt", 'r', encoding='utf8')
f.readline()
cnt = 0
for s in f:
    t = s.split('\t')[1:]
    if t[0]=='1' and (int(t[1])>=85 or int(t[2])>=85):
        cnt += 1
print(cnt)
#
# print('6100' >= '6 85')
# print('100' >= '85')
# print(ord('1'), ord(' '))
