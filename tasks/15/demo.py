def f(A,x):
    return ((x%2==0) <= (not(x%3==0))) or (x + A >= 100)

for A in range(1, 100):
    for x in range(1,500):
        if f(A,x) == False:
            break
    else:
        print(A)
        break
