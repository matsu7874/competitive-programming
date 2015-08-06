(N,M) = [int(x) for x in input().split()]
h = [[0 for j in range(N)] for i in range(N)]
for i in range(M):
    (a,b,c) = [int(x) for x in input().split()]
    for j in range(c):
        for k in range(j+1):
            h[a+j-1][b+k-1] = 1
Q = int(input())
for i in range(Q):
    cnt = 0
    (a,b,c) = [int(x) for x in input().split()]
    for j in range(c):
        cnt += h[a+j-1][b+0-1:b+j].count(0)
    print(cnt)