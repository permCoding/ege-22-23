f = open("demo.txt")
f.readline()
numbers = [int(line) for line in f]
print(numbers[-10:])

# f = [1,3,4,22,0]
# lst = [str(n) for n in f]
# print(lst)