for a in range(1,100):
    flag =0
    for x in range(1,1000):
        for y in range(1, 1000):
            if ((x > a) or (y > x) or ((2*y + x) < 110)) == 0:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        print(a)