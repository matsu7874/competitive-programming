import random


def is_prime(n):
    # 素数判定
    if n == 2:
        return True
    elif n < 2 or n & 1 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def miller_rabin_test(n, k=100):
    # 確率素数判定　間違う確率は4^-k
    if n == 2:
        return True
    if n < 2 or n & 1 == 0:
        return False
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(k):
        a = random.randint(1, n- 1)
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = pow(y, 2, n)
            t <<= 1
        if y != n - 1 and t & 1 == 0:
            return False
    return True


def prime_sieve(n):
    # 素数リスト(エラトステネスの篩)
    # N以下の素数のリストを返す
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(4, n + 1, 2):
        is_prime[i] = False
    for i in range(3, int(n**0.5 + 1), 2):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def prime_decomposition(n):
    # 素因数分解
    if n < 2:
        return []
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n >>= 1

    while n % 3 == 0:
        prime_factors.append(3)
        n //= 3

    a = 5
    b = 7
    while a ** 2 <= n:
        if n % a == 0:
            prime_factors.append(a)
            n //= a
        elif n % b == 0:
            prime_factors.append(b)
            n //= b
        else:
            a += 6
            b += 6
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def prime_decomposition_use_prime_list(n, sorted_prime_list=[]):
    # 素因数分解
    prime_factors = []
    if n < 2:
        return prime_factors
    i = 0
    while sorted_prime_list[i]**2 <= n:
        if n % sorted_prime_list[i] == 0:
            prime_factors.append(sorted_prime_list[i])
            n //= sorted_prime_list[i]
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


if __name__ == '__main__':
    for i in range(3,100):
        print(i,miller_rabin_test(i))
    print(miller_rabin_test(1000000000000037))
    print(miller_rabin_test(9999999999999937))
