import collections

def prime_decomposition(n):
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

n = int(input())
freq = collections.Counter(prime_decomposition(n))
ans = n
for k,v in freq.items():
    ans *= (1-1/k)
print(int(ans))
