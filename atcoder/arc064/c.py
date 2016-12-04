n,x = map(int, input().split())
a = list(map(int, input().split()))
b = a[::-1]

def solve(a):
    total = 0
    if a[0] > x:
        total += a[0]-x
        a[0] = x

    for i in range(1, n):
        if a[i-1] + a[i] > x:
            d = (a[i-1] + a[i]) - x
            total += d
            a[i] = max(0, a[i] - d)
    return total

print(min(solve(a), solve(b)))
