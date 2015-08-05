def main():
    N =int(input())
    start, gool = [int(x) for x in input().split()]
    C = [[int(x) for x in input().split()] for i in range(N+1)]
    C[N] = [gool ,gool]
    res = 0

    x = start
    y = 0
    memo = [[0,start], [0,start]]
    slope = [-10000000, 10000000]
    i = 1
    while i<=N:
        l = C[i][0]
        r = C[i][1]
        if slope[0]*(i-y) < (l-x):
            slope[0] = (l-x)/(i-y)
            memo[0][0] = i
            memo[0][1] = l
        if slope[1]*(i-y) > (r-x):
            slope[1] = (r-x)/(i-y)
            memo[1][0] = i
            memo[1][1] = r
        if slope[0] > slope[1]:
            if memo[0][0] == i:
                res += ((memo[1][0]-y)**2 + (memo[1][1]-x)**2)**0.5
                x = memo[1][1]
                y = memo[1][0]
            else:
                res += ((memo[0][0]-y)**2 + (memo[0][1]-x)**2)**0.5
                x = memo[0][1]
                y = memo[0][0]
            slope[0], slope[1] = -10000000, 10000000
            i = y
        i += 1
    print(res + ((N-y)**2 + (gool-x)**2)**0.5)

def hypot(a, b):
    return (a * a + b * b)**0.5

def main2():
    n =int(input())
    start, gool = [int(x) for x in input().split()]
    C = [[int(x) for x in input().split()] for i in range(n+1)]
    C[0] = [start, start]
    C[n] = [gool ,gool]

    ql = [0 for i in range(n+1)]
    qr = [0 for i in range(n+1)]
    lmin = 0
    lmax = 0
    rmin = 0
    rmax = 0

    distance = 0.0
    x = start
    y = 0
    for i in range(1,n+1):
        while lmax > lmin:
            lmax -= 1
            py = ql[lmax]
            px = C[py][0]
            ppy = y
            ppx = x
            if lmax > lmin:
                ppy = ql[lmax-1]
                ppx = C[ppy][0]
            if ((px - ppx) / (py - ppy) > (C[i][0] - px) / (i - py)):
                lmax += 1
                break
        while rmax > rmin:
            rmax -= 1
            py = qr[rmax]
            px = C[py][1]
            ppy = y
            ppx = x
            if (rmax > rmin):
                ppy = qr[rmax - 1]
                ppx = C[ppy][1]
            if ((ppx - px) / (ppy - py) < (C[i][1] - px) / (i - py)):
                rmax += 1
                break
        ql[lmax] = qr[rmax] = i
        lmax += 1
        rmax += 1
        while ((C[ql[lmin]][0] - x) * (qr[rmin] - y)  > (C[qr[rmin]][1] - x)*(ql[lmin] - y)):
            if (ql[lmin] < qr[rmin]):
                distance += hypot((y - ql[lmin]), (x - C[ql[lmin]][0]))
                y = ql[lmin]
                x = C[y][0]
                lmin += 1
            else:
                distance += hypot((y - qr[rmin]), (x - C[qr[rmin]][0]))
                y = qr[rmin]
                x = C[y][0]
                rmin += 1
    while (lmin < lmax) :
        distance += hypot((y - ql[lmin]), (x - C[ql[lmin]][0]))
        y = ql[lmin]
        x = C[y][0]
        lmin += 1
    print(distance)

if __name__ == '__main__':
    main2()
