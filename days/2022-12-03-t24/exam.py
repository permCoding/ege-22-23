a, b, s = 0, 9, ''
while a < b:
    # a = 0 1 2 3 4   5
    # b = 9 8 7 6 5   4
    a, b = a+1, b-1
    s += '8'
print(s)

a, b, s = 0, 5, '8'
while a < b:
    # a = 0 1 2   3 
    # b = 5 4 3   2      
    a, b = a+1, b-1
    s *= 2  # 88  8888  88888888
print(s)
