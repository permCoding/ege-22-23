for i in range(123450708,123460000):
    if (i%23==0) and (i%10==8) and ((i//100)%10==7):
        print(i, i//23)
