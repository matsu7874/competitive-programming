"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def main():
    res = 0
    num = 1
    den = 1
    for a in range(1,10):
        for b in range(1,10):
            for c in range(a,10):
                for d in range(1,10):
                    if a*10+b >= c*10+d:
                        continue
                    if a==d and (a*10+b)*c==b*(c*10+d):
                        num *= b
                        den *= c
                    if b==c and (a*10+b)*d==a*(c*10+d):
                        num *= a
                        den *= d
    print(den//gcd(num,den))


if __name__ == '__main__':
    main()
