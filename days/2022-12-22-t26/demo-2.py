f = open("demo.txt")
f.readline()
numbers = []
while True:
    line = f.readline()
    if not line: break
    numbers += [int(line)]

print(numbers[-1])