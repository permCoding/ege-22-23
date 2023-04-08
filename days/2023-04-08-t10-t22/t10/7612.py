import re

txt = open('demo-2023-10.txt').read()

lst = re.findall('[^а-я][вВ]ечер[^а-я]', txt)
print(len(lst))
print(lst) # [' вечер ', ' вечер;']

lst = re.findall('[^а-я]вечер[а-я]+', txt)
print(len(lst))
for elm in lst: print(elm)

'''
[а-я][Вв]ечер[^а-я] = 0 - заканчиваются на вечер
[^а-я][Вв]ечер[а-я] = 40 - начинаются на вечер
[а-я]вечер[а-я] = __ - 'вечер' внутри слова
[а-я](вечер|Вечер)[а-я] = __ - 'вечер' внутри слова
[а-я][вВ]ечер[а-я] = 0 - 'вечер' внутри слова
'''
