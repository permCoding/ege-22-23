import re

lst = [
    '1021394',  # True
    '102139456',
    '55510213977777456',
    '19213974',  # True
]
ptn = '^1.2139.*4$'
for elm in lst:
    if re.match(ptn, elm):
        print(elm)

"""
. - это один любой символ
.* - это любое кол-во любых символов, в том числе и ноль символов
.+ - это один и более любых символов
"""