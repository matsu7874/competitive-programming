def prime_decomposition(n):
    # 素因数分解
    prime_factors = []
    if n < 2:
        return prime_factors
    while n >= 2 and n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2
    if n > 1:
        prime_factors.append(n)
    return prime_factors

X = int(input())
p = prime_decomposition(X)
Y = 1
while p:
    if len(p) == 1:
        Y *= p[0]
        p.pop()
    elif p[-1] == p[-2]:
        p.pop()
        p.pop()
    else:
        Y *= p.pop()
print(Y)
