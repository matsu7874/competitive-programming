def mod_pow(x, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n //= 2
    return res

N = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
f = [0] * N

for i in range(N):
    f[A[i]] += 1
if A[0] > 0 or f[0] > 1:
    print(0)
    exit()
max_a = max(A)
total = 1
for i in range(1, max_a + 1):
    if f[i] == 0:
        print(0)
        exit()
    total *= mod_pow(mod_pow(2, f[i - 1], mod) - 1, f[i], mod)
    total *= mod_pow(2, f[i] * (f[i] - 1) // 2, mod)
    total %= mod
print(total)
