def get_divisors(n):
    # 約数列挙
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    list(divisors)
    return divisors

n = int(input())
if n % 2 == 1:
    print(sum(get_divisors(n)))
    exit()
divisors = [get_divisors(n), get_divisors(n - 1)]
total = 0
for d in divisors[0]:
    if d * 2 in divisors[0] or d in divisors[1]:
        total += d
print(total)
