def get_divisors(n):
    # 約数列挙
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

N = int(input())
s = sum(get_divisors(N)) - N

if N < s:
    print('Abundant')
elif N == s:
    print('Perfect')
else:
    print('Deficient')
