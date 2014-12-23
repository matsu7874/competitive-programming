while True:
    (n, m) = [int(x) for x in input().split()]
    if n==0 and m==0:
        exit()
    a = []
    b = []
    for i in range(n):
        a.append(int(input()))
    for i in range(m):
        b.append(int(input()))
    a_sum = sum(a)
    b_sum = sum(b)
    target = a_sum - b_sum
    found = False
    for ai in a:
        for bi in b:
            if (ai-bi)*2 == target:
                print(ai, bi)
                found = True
            if found:
                break
        if found:
            break
    if found == False:
        print(-1)
