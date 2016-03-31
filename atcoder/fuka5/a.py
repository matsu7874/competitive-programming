while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        exit()
    x = list(map(int, input().split()))
    x.sort()
    total = 0
    for i in range(k):
        total += x[i]
    print(total)
