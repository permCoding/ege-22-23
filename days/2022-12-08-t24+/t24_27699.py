# https://inf-ege.sdamgia.ru/problem?id=27699

s = open('t24_27699.txt').readline()

p = s.find('LDR'*5)
print(s[p:p+15+3])
