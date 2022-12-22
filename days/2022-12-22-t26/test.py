line = "12 34 563 77 9"
print(line[0:-2])

lst = line.split()
print(lst)
print(lst[0:-2])

print(lst[::1])
print(lst[::2])
print(lst[::-1])
