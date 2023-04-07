import re

txt = open("./10_7260.txt").read()

#print(txt.count("куда"))
#print(txt.count("Куда"))

lst = re.findall('куда[а-я]+', txt, re.I)
print(len(lst))

lst = re.findall('[а-я]+куда', txt, re.I)
print(len(lst))

'''
в ворде:
[а-я][Чч]ас[а-я]  = 65   _час_
[а-я][Чч]ас[!а-я] = 96   _час
[!а-я][Чч]ас[а-я] = 110  час_
'''
