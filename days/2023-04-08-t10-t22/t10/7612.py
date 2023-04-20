import re

#txt = open('10_7612.txt', encoding='utf8').read()
txt = open('10_7612.txt').read()

#lst = re.findall('[^а-я][вВ]ечер[^а-я]', txt)
#print(len(lst)) # это отдельные слова
#print(lst) # [' вечер ', ' вечер;']

lst = re.findall('[^а-я]вечер[а-я]+', txt, re.I)
print(len(lst)) # слова которые начинаются на вечер...
print(lst)

lst = re.findall('[а-я]+вечер[^а-я]', txt, re.I)
print(len(lst)) # слова которые заканчиваются на ...вечер
print(lst)

lst = re.findall('[а-я]+вечер[а-я]+', txt, re.I)
print(len(lst)) # слова в которых внутри ...вечер...
print(lst)

'''V
[а-я][Вв]ечер[^а-я] = 0 - заканчиваются на вечер
[^а-я][Вв]ечер[а-я] = 40 - начинаются на вечер
[а-я]вечер[а-я] = __ - 'вечер' внутри слова
[а-я](вечер|Вечер)[а-я] = __ - 'вечер' внутри слова
[а-я][вВ]ечер[а-я] = 0 - 'вечер' внутри слова
'''
