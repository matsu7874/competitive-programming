(n, t) = [int(x) for x in input().split()]
f = [0 for i in range(t+1)]
for i in range(n):
    a = int(input())
    j = 1
    while a*j <= t:
        f[a*j] += 1
        j += 1
print(max(f))
