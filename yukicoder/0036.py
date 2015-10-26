def get_divisors(n):
    # 約数列挙
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return list(divisors)

N = int(input())
d = get_divisors(N)
if len(d) > 4:
    print('YES')
elif len(d) == 4:
    d.sort()
    if d[1] * d[1] == d[2]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
