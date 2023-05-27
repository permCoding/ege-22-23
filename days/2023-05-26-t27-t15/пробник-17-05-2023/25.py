for n in range(1, 10**8+1, 253):
    s = str(n)
    if s[:2] == '12' and s[4:6] == '15' and s[-1]=='6':
        print(n, n//253)
