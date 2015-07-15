"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_arithmetic_sequence(a, d, n):
    return n*a + (n-1)*n*d//2

def main():
    n = 1000 - 1
    print(sum_arithmetic_sequence(3, 3, n//3) + sum_arithmetic_sequence(5, 5, n//5) - sum_arithmetic_sequence(15, 15, n//15))


if __name__ == '__main__':
    main()
