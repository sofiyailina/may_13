with open("27-A_demo (3).txt") as f:
    n = int(f.readline())
    maxsum = 0
    mindif = 100_000
    for line in f:
        a, b = map(int, line.split())
        maxsum += max(a,b)



    if maxsum % 3 != 0:
        maxsum -= mindif
    print(maxsum)