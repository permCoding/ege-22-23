# https://inf-ege.sdamgia.ru/problem?id=37369
from time import monotonic as m

nums = [int(x) for x in open("17.txt")] 

start = m()
count, mx_d = 0, 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        a, b = nums[i], nums[j]
        if abs(a-b) % 80 == 0:
            count += 1
            mx_d = max(mx_d, abs(a-b))
finish = m()
print(count, mx_d)
print(finish-start)


'''
В файле содержится последовательность из 10000 целых положительных чисел. 
Каждое число не превышает 10000. Определите и запишите в ответе сначала 
количество пар элементов последовательности, у которых разность элементов 
кратна 80, затем максимальную из разностей элементов таких пар. В данной 
задаче под парой подразумевается два различных элемента последовательности.
a b
b a
'''
