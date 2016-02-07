"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors

def main():
    upper_limit = 28124
    res = 0
    abundants = []
    for i in range(1, upper_limit):
        if i < sum(get_divisors(i)) - i:
            abundants.append(i)
    num_abundants = len(abundants)
    writable = set()
    for i in range(num_abundants-1):
        writable.add(abundants[i]*2)
        for j in range(i+1, num_abundants):
            writable.add(abundants[i] + abundants[j])
    for i in range(1, upper_limit):
        if i not in writable:
            res += i
    print(res)

if __name__ == '__main__':
    main()
