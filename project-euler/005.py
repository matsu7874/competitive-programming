"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
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

def prime_decomposition(n, sorted_prime_list=[]):
    prime_factors = []
    if n<2:
        return prime_factors
    if sorted_prime_list == []:
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
    else:
        i = 0
        while sorted_prime_list[i]**2 <= n:
            if n%sorted_prime_list[i] == 0:
                prime_factors.append(sorted_prime_list[i])
                n //= sorted_prime_list[i]
            else:
                i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def main():
    target = 20
    prime_list = prime_sieve(target)
    dic = {key:0 for key in prime_list}
    for i in range(target + 1):
        prime_factors = prime_decomposition(i, prime_list)
        for p in prime_list:
            dic[p] = max(dic[p], prime_factors.count(p))
    ans = 1

    for k,v in dic.items():
        ans *= k**v
    print(ans)

if __name__ == '__main__':
    main()
