def combination(n, r):
    res = 1
    t = r - 1
    while t >= 0:
        res = res * (n - t) // (r - t)
        t -= 1
    return res

N, K = map(int, input().split())
ave = K // N
rem = K % N
pattern = combination(N,rem)%(10**9+7)
if K<N:
    pattern = combination(N+K-1,K)%(10**9+7)
print(pattern)
