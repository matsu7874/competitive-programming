"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""


def factrial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def main():
    t = factrial(100)
    res = 0
    while t>0:
        res += t%10
        t //= 10
    print(res)

if __name__ == '__main__':
    main()
