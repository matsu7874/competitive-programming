# Lagrange interpolation
def inv(n, mod):
    a = n
    b = mod
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    return u

mod = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))
T = int(input())

if T <= N:
    print(A[T])
    exit()


factorial = [1] * (N + 1)
for i in range(1, N + 1):
    factorial[i] = factorial[i - 1] * i % mod

numer_p = 1
for i in range(N + 1):
    numer_p = numer_p * (T - i + mod) % mod

total = 0
for i in range(N + 1):
    numer = numer_p * inv(T - i, mod)
    denom = factorial[N - i] * factorial[i]
    if (N - i) % 2 == 1:
        denom *= -1
    total += A[i] * numer * inv(denom, mod)

print(total % mod)
