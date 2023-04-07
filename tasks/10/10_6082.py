import re


txt = open('10_6082.txt').read()

lst = re.findall('.род.', txt, re.I)
print(len(lst))

lst = re.findall('[^а-я]род[^а-я]', txt, re.I)
print(len(lst))
