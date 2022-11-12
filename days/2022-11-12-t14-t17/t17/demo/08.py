# найти сумму нечётных чисел из строки

line = '1,2,0,4,5,6,77,8'  # print(line.split(','))

print(sum([int(x) for x in line.split(',') if int(x)%2]))
