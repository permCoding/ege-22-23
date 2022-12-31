cnt = 0
for e in open("09_5126.csv"):
    a = list(map(int, e.split(";")))
    b = [n for n in a if a.count(n) == 3]
    c = [n for n in a if a.count(n) == 1]
    if len(b) == 3 and len(c) == 3 and sum(c)/3 <= sum(b):
        print(b, c)
        cnt += 1
print(cnt)

"""
– в строке только одно число повторяется ровно три раза, остальные числа различны;
– среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
"""