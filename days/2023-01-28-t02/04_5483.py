def f(x,y,z,w):
    return (z==(1-x)) <= ((w<=(1-y)) and (y<=x))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x,y,z,w) == True:
                    print(y,z,x,w)
##                    print(_,_,_,w)
##                    print(_,_,_,z)
"""
- 0 -
1 1 0 0 +
1 1 0 1 ~
1 0 1 1 ~
- 1 -
1 0 1 1 -
1 1 1 0 +
"""
