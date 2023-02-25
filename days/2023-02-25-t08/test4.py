start, finish = '10000', '77777'
a, b = int(start, 8), int(finish, 8)

for elm in range(a, b+1):
    print(elm, oct(elm)[2:])



##int()
##bin() 0b
##oct() 0o
##hex() 0x
