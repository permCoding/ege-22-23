def f(x,y,z,w):
    return (w <= (y==z)) and (y == (z<=x))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w) == False:
                    print(z,w,y,x)
"""
- 0 -
0 1 0 0
0 0 0 1 +
- 1 -
1 0 0 0 +
0 0 1 1 +
1 0 1 1
"""