def lcg(x, a, b, c):
    return (x*a+b)%c


while True:
    (N, A, B, C, X) = [int(x) for x in input().split()]
    if N==0 and A==0 and B==0 and C==0 and X==0:
        exit()
    Y = [int(x) for x in input().split()]
    i = 0
    len_y = len(Y)
    for j in range(len_y):
        if X == Y[j]:
            if j == len_y-1:
                break
            X = lcg(X, A, B, C)
            i += 1
            continue
        else:
            while X != Y[j]:
                X = lcg(X, A, B, C)
                i += 1
                if i > 10000:
                    break
            if j != len_y-1:
                X = lcg(X, A, B, C)
                i += 1
        if i > 10000:
            i = -1
            break
    print(i)