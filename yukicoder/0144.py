N, p = input().split()
N = int(N)
p = 1 - float(p)
e = [1.0] * (N + 1)
for i in range(2, N + 1):
    j = 2 * i
    while j <= N:
        e[j] *= p
        j += i
print(sum(e[2:]))
