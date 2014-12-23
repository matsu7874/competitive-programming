while True:
    (n, p) = [int(x) for x in input().split()]
    if n==0 and p==0:
        exit()
    s = [0 for _ in range(n)]
    i = 0
    q = p
    while True:
#        print(i,q,s)
        if q == 0:
            q = s[i]
            s[i] = 0
        else:
            s[i] += 1
            q -= 1
            if q==0 and s[i]==p:
                print(i)
                break
        i = (i+1)%n
