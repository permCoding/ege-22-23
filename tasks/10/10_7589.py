'''
- в ворде:
[а-я]{1,}[Чч]ас[а-я]  = 65   _час_
[а-я][Чч]ас[!а-я] = 96   _час
[!а-я][Чч]ас[а-я] = 110  час_
- в Libre Office Writer
([а-я]+час)|(час[а-я]+)|([а-я]+час[а-я]+)
'''
import re

txt = open("./10_7589.txt").read()

print(txt.count("час"))
print(txt.count("Час"))

lst = re.findall('[Чч]ас', txt)
print(len(lst))

lst = re.findall('час', txt, re.I)
print(len(lst))

lst = re.findall('[^а-я]час[а-я]', txt, re.I)
n_ = len(lst)
print(n_)
# for e in lst: print(e)

lst = re.findall('[а-я]час[^а-я]', txt, re.I)
_n = len(lst)
print(_n)
# for e in lst: print(e)

lst = re.findall('[а-яА-Я][чЧ]ас[а-яА-Я]', txt)
_n_ = len(lst)
print(_n_)

print(n_ + _n + _n_)

