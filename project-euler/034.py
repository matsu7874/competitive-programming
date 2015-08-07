"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def each_digits(n, base=10):
    digits = []
    a = 1
    while n >= a:
        digits.append(n//a % base)
        a *= base
    return digits[::-1]

def factrial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def main():
    res = 0
    for i in range(10**6):
        if i == sum([factrial(t) for t in each_digits(i)]):
            res += i
    print(res)


if __name__ == '__main__':
    main()
