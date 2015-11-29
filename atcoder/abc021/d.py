def combination(n, r):
    res = 1
    t = r - 1
    while t >= 0:
        res = res * (n - t) // (r - t)
        t -= 1
    return res

n = int(input())
k = int(input())

print(combination(n+k-1,k) % 1000000007)
