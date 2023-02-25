for u in range(1, 10):
    for h in range(1, 10):
        for v in range(1, 10):
            for m in range(0, 10):
                sla = u*10+m
                slb = h*100+u*10+m
                res = v*100+m*10+h
                if sla + slb == res:
                    if len(set([u,h,v,m]))==4:
                        print(sla, slb, res)
#  87
# 487
# 574