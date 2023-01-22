def f(x,y,z,w):
    return (z<=x) <= (w or (1-y))

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not(f(x,y,z,w)):
                    # print(z,x,w,y)
                    print(x,y,z,w)

# y w x z
# p1p2p3p4
# 0 1 0 0
# 1 1 0 0
# 1 1 1 0
