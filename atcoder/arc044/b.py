N = int(input())
A = list(map(int, input().split()))
f = [0] * 100000
mod = 1000000007


power = [2]
i = 0
while 2**i < 1000000007:
    power.append(power[i] * power[i] % 1000000007)
    i += 1
bit_max = i

def pow2(n):
    a = 1
    for i in range(bit_max + 1):
        if n & power[i]:
            a *= power[i]
    return a


for a in A:
    f[a] += 1

if A[0] == 0 and f[0] == 1:
    total = 1
    if N == 1:
        print(total)
        exit()
else:
    print(0)
    exit()

max_a = max(A)
for i in range(1, max_a + 1):
    if f[i] == 0:
        print(0)
        exit()
    else:
        t = pow2(f[i - 1] - 1)% mod
        total *= t ** f[i] % mod
        total *= pow2(f[i] * (f[i] - 1) // 2) % mod
        # t = (2**f[i - 1] - 1) % mod
        # total *= t ** f[i] % mod
        # total *= 2**(f[i] * (f[i] - 1) // 2) % mod

        total %= mod
print(total)
