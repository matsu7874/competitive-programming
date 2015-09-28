def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
N = int(input())
if N == 1:
    print('Not Prime')
elif is_prime(N):
    print('Prime')
elif N % 3 > 0 and N % 10 in (1, 3, 7, 9):
    print('Prime')
else:
    print('Not Prime')
