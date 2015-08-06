"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def sum_geometric_sequence(a, r, n):
    if r == 0:
        return a
    return a * (1-r**n) // (1-r)

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

def get_degree(lst):
    degree = {}
    for i in lst:
        degree.update({i:lst.count(i)})
    return degree

def main():
    prime_list = prime_sieve(10000)
    sum_divisors = []
    for i in range(10000):
        D = get_degree(prime_decomposition(i, prime_list))
        t = 1
        for k,v in D.items():
            t *= sum_geometric_sequence(1, k, v+1)
        sum_divisors.append(int(t - i))
    res = 0
    for i in range(10000):
        for j in range(i+1, 10000):
            if sum_divisors[j] == i and sum_divisors[i] == j:
                res += i + j
    print(res)

if __name__ == '__main__':
    main()
