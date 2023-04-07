import re

txt = open("./10_7260.txt").read()

print(txt.count("куда"))
print(txt.count("Куда"))
n = re.findall('куда[]', txt, re.I)
print(txt.count("куда"))
'''
в ворде:
[а-я][Чч]ас[а-я]  = 65   _час_
[а-я][Чч]ас[!а-я] = 96   _час
[!а-я][Чч]ас[а-я] = 110  час_
'''