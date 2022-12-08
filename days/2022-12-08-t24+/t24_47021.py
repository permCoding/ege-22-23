# https://inf-ege.sdamgia.ru/problem?id=47021
# s = 'BABCCABABCAACCACCCCCCCCCABCCCCCCCBA'
s = open('./t24_47021.txt').readline()

lst = s.split('A')
lst = [elm for elm in lst[1:-1] if len(elm)>=8]
lst = [elm for elm in lst if 'B' not in elm]

print(len(lst))

# print(len([elm for elm in open('./t24_47021.txt').readline().split('A')[1:-1] if len(elm)>=8 and 'B' not in elm]))

'''
Текстовый файл содержит только заглавные буквы 
латинского алфавита (ABC…Z). Определите количество 
групп из идущих подряд не менее 10 символов, 
которые начинаются и заканчиваются буквой A и не содержат 
других букв A (кроме первой и последней) и букв B.
'''