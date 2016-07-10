import itertools
import functools
import operator

def prime_decomposition(n):
    if n < 2:
        return []
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n >>= 1
    while n % 3 == 0:
        prime_factors.append(3)
        n //= 3
    a = 5
    b = 7
    while a ** 2 <= n:
        if n % a == 0:
            prime_factors.append(a)
            n //= a
        elif n % b == 0:
            prime_factors.append(b)
            n //= b
        else:
            a += 6
            b += 6
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def get_divisor(n):
    prime_divisor = prime_decomposition(n)
    divisor = [1] + prime_divisor
    for i in range(2, len(prime_divisor)+1):
        for d in itertools.combinations(prime_divisor, r=i):
            divisor.append(functools.reduce(operator.mul, d))
    return divisor


def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    length = [0 for i in range(10**6 + 1)]
    max_length = 1
    for e in x:
        length[e] = max(length[e], *[length[d] + 1 for d in get_divisor(e)])
        max_length = max(max_length, length[e])
    print(max_length)


import cProfile
cProfile.run( 'main()' ) 