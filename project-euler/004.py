"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindromic(n, base=10):
    a = []
    i = 0
    while n>0:
        a.append(n%base**(i+1)//base**i)
        n //= 10
    l = len(a)
    if all([a[i]==a[l-i-1] for i in range(l//2)]):
        return True
    else:
        return False

def main():
    ans = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            if is_palindromic(a*b) and a*b>ans:
                ans = a*b
    print(ans)


if __name__ == '__main__':
    main()
