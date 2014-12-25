while True:
    n = int(input())
    if n==0:
        exit()
    cnt = 0
    i = 2
    while i*(i+1) <= n*2:
        a =int(n/i-(i-1)/2) 
        if a*i + (i-1)*i/2 == n:
            cnt += 1
        i += 1
    print(cnt)