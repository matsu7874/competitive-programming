"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def prime_decomposition(n):
    prime_factors = []
    if n<2:
        return prime_factors
    while n >= 2 and n%2 == 0:
        prime_factors.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def main():
    target = 600851475143
    print(max(prime_decomposition(target)))
if __name__ == '__main__':
    main()
