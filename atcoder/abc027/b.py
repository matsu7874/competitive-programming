N = int(input())
A = [int(x) for x in input().split()]
sum_A = sum(A)
if sum_A%N != 0:
    print(-1)
else:
    target = sum_A // N
    cnt = 0
    p = 0
    n = 0
    for i in range(N):
        p += A[i]
        n += 1
        if p == n*target:
            cnt += n-1
            p = 0
            n = 0
    print(cnt)