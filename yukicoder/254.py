import itertools

N, K = [int(x) for x in input().split()]

def prime_factorize(n):
    prime_factors = []
    if n == 1:
        return 1
    while n%2 == 0:
        prime_factors.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        prime_factors.append(n)
    return prime_factors

A = prime_factorize(N)

D = [1]
for i in range(1,len(A)+1):
    for a in itertools.combinations(A,i):
        d = 1
        for ai in a:
            d *= ai
        D.append(d)
D = list(set(D))
D.sort()

print(D[-2])