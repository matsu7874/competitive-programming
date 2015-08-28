def prime_sieve(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(4, n+1, 2):
        is_prime[i] = False
    for i in range(3, int(n**0.5+1), 2):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def using_digits(n, base=10):
    digits = set()
    while n > 0:
        digits.add(n % base)
        n //= base
    return digits

N = int(input())
A = map(int, input().split())
primes = prime_sieve(5000000)
length_primes = len(primes)
digits = [using_digits(p) for p in primes]
digits_count = [0 for i in range(10)]
max_gap = 0
k = 0
l = 0
h = 0
t = 0


print(using_digits(N))
