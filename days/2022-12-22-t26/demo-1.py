f = open("demo.txt")
line = f.readline()

n = int(line)
numbers = []
for i in range(n):
    line = f.readline()
    numbers.append(int(line))

print(numbers[-1])