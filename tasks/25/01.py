for i in range(2023, 10**10, 2023):
    s = str(i)
    if s[0]=='1' and s[2:6]=='2139' and s[-1]=='4':
        print(i, i//2023)
