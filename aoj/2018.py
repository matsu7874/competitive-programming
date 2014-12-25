while True:
    (n, m, p) = [int(x) for x in input().split()]
    if n==0 and m==0 and p==0:
        exit()
    X = []
    for i in range(n):
        X.append(int(input()))
    if X[m-1] == 0:
        print(0)
    else:
        print(int(sum(X)*(100-p)/X[m-1]))
