def main():
    while True:
        n,m,a = [int(x) for x in input().split()]
        if n==0 and m==0 and a==0:
            return
        L = []
        for i in range(m):
            h,p,q = [int(x) for x in input().split()]
            L.append((h,p-1,q-1))
        L.sort()
        res = [i+1 for i in range(n)]
        for l in L:
            res[l[1]], res[l[2]] = res[l[2]], res[l[1]]
        print(res[a-1])

if __name__ == '__main__':
    main()
