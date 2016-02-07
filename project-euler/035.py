"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
def is_prime(n):
    if n == 2:
        return True
    elif n<2 or n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def main():
    cnt = 0
    for i in range(2,1000000):
        flg = True
        t = i
        for j in range(len(str(i))):
            t = t//(10**(len(str(i))-1)) + t%(10**(len(str(i))-1))*10
            if not is_prime(t):
                flg = False
                break
        if flg:
            cnt += 1
            # print(i)
    print(cnt)
if __name__ == '__main__':
    main()
