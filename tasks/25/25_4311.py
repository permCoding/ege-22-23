for i in range(27, 10**8, 27):
    s = str(i)
    if s[0:3]=='123' and s[-3:]=='890':
        print(i, i//27)
