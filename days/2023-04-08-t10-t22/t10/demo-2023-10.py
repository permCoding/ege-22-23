import re

txt = open('demo-2023-10.txt').read()
lst = re.findall('[^а-я]теперь[^а-я]', txt)
print(len(lst))
