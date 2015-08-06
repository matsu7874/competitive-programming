(n, m) = [int(x) for x in input().split()]
F = [1 for i in range(m)]
for i in range(n):
    F[int(input())-1] += 1
p = 1
for f in F:
    p *= f
print((p-1)%1000000007)
