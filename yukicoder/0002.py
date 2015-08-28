def prime_decomposition(n):
    prime_factors = {}
    if n < 2:
        return prime_factors
    while n >= 2 and n % 2 == 0:
        if 2 not in prime_factors:
            prime_factors.update({2: 1})
        else:
            prime_factors[2] += 1
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            if i not in prime_factors:
                prime_factors.update({i: 1})
            else:
                prime_factors[i] += 1
            n //= i
        else:
            i += 2
    if n > 1:
        if n not in prime_factors:
            prime_factors.update({n: 1})
        else:
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
