for u in range(1, 10):
    for d in range(1, 10):
        for a in range(0, 10):
            for r in range(0, 10):
                for k in range(0, 10):
                    sla = d*10000+u*1000+r*100+a*10+k
                    slb = u*1000+d*100+a*10+r
                    res = d*10000+r*1000+a*100+k*10+a
                    if sla + slb == res:
                        if len(set([u,d,a,r,k])) == 5:
                            print(sla)
# 8126 16252