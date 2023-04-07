import re


txt = open('10_7082.txt').read()

lst = re.findall('[^а-я]Офицер[^а-я]', txt)
print(len(lst))
