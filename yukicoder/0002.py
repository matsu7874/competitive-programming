def prime_decomposition(n):
    import collections
    prime_factors = collections.Counter()
    while n >= 2 and n % 2 == 0:
        prime_factors[2] += 1
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            prime_factors[i] += 1
            n //= i
        else:
            i += 2
    if n > 1:
        prime_factors[n] += 1
    return prime_factors

N = int(input())
win = 0
for p, v in prime_decomposition(N).items():
    win = win ^ v
if win != 0:
    print('Alice')
else:
    print('Bob')
