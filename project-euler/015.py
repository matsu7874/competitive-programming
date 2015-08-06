"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

def combination(n, r):
    res = 1
    t = r-1
    while t >= 0:
        res = res*(n-t)//(r-t)
        t -= 1
    return res

def main():
    print(combination(40,20))

if __name__ == '__main__':
    main()
