f = open("27423.txt")
line = f.readline()
s, n = map(int, line.split())
nums = [int(line) for line in f]

nums.sort()

res = []
for i in range(n):
    if sum(res) + nums[i] > s: break
    res += [nums[i]]

res.pop()
for j in range(n-1, 0, -1):
    if sum(res) + nums[j] <= s:
        res += [nums[j]]
        break
print(len(res), nums[j])
# print(len(res), res[-1])

"""
определите максимальное число файлов можно сохранить в архиве, 

а также максимальный размер имеющегося файла, 
который может быть сохранён в архиве, 
при условии, что сохранены файлы 
максимально возможного числа пользователей
"""