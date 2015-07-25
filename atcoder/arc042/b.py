def main():
    tx,ty = [int(z) for z in input().split()]
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = [int(z) for z in input().split()]
        X.append(x)
        Y.append(y)
    ans = 100
    for i in range(N):
        if X[i-1] == X[i]:
            ans = min(ans, abs(X[i]-tx))
        else:
            a = (Y[i-1]-Y[i])/(X[i-1]-X[i])
            b = -1
            c = -(Y[i-1]-Y[i])/(X[i-1]-X[i])*X[i] + Y[i]
            d = abs(a*tx + b*ty + c)/((a**2+b**2)**0.5)
            ans = min(ans, d)
    print(ans)

if __name__ == '__main__':
    main()
