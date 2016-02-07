"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

import itertools

def main():
    res = set()
    for t in itertools.permutations([1,2,3,4,5,6,7,8,9]):
        a = t[0]*10 + t[1]
        b = t[2]*100 + t[3]*10 + t[4]
        c = t[5]*1000 + t[6]*100 + t[7]*10 +t[8]
        if a*b == c:
            res.add(c)
        a = t[0]
        b =  t[1]*1000 + t[2]*100 + t[3]*10 + t[4]
        c = t[5]*1000 + t[6]*100 + t[7]*10 +t[8]
        if a*b == c:
            res.add(c)
    print(sum(res))

if __name__ == '__main__':
    main()
