# https://inf-ege.sdamgia.ru/problem?id=47021
# s = 'BABCCACABCAACCCCCCCCCCCCCCCCCABABB'
s = open('./t24_47021.txt').readline()

lst, tmp = [], ''
for i in range(len(s)):
    if s[i] == 'A':
        tmp += s[i]
        if len(tmp)>=10 and tmp[0]=='A' and 'B' not in tmp:
            lst += [tmp]
        tmp = 'A'
    else:
        tmp += s[i]

print(len(lst))

'''
Текстовый файл содержит только заглавные буквы 
латинского алфавита (ABC…Z). Определите количество 
групп из идущих подряд не менее 10 символов, 
которые начинаются и заканчиваются буквой A и не содержат 
других букв A (кроме первой и последней) и букв B.
'''