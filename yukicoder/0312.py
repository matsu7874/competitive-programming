def get_divisors(n):
    # 約数列挙
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return list(divisors)

N = int(input())
ds = get_divisors(N)
ds.sort()
for d in ds:
    if d > 2:
        print(d)
        exit()
