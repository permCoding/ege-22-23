lines = open("demo.txt").readlines()
numbers = [int(line) for line in lines[1:]]
# numbers = list(map(int, lines))[1:]
print(numbers)