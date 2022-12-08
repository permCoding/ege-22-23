# https://inf-ege.sdamgia.ru/problem?id=27697
#s = 'RDDRLLDDDLD'

print(len(max(open('t24_27697.txt') \
              .readline() \
              .replace('R',' ') \
              .replace('L',' ') \
              .split())))
