"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
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

def main():
    target = 2000000
    print(sum(prime_sieve(target)))

if __name__ == '__main__':
    main()
