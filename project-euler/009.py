"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def main():
    target = 1000
    for c in range(target//3, target//2):
        for b in range((target-c)//2, target-c):
            a = (target-c-b)
            if c**2 == b**2 + a**2:
                print(a*b*c)
if __name__ == '__main__':
    main()
