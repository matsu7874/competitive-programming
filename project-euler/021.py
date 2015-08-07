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

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors

def main():
    sum_divisors = [sum(get_divisors(i)) - i for i in range(10000)]
    res = 0
    for i in range(10000):
        for j in range(i+1, 10000):
            if sum_divisors[j] == i and sum_divisors[i] == j:
                res += i + j
    print(res)

if __name__ == '__main__':
    main()
