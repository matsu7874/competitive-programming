import math


def sum_each_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


N = int(input())
acceptables = []
lower_limmit = max(1, int(N - math.ceil(math.log10(N)) * 9))
for i in range(lower_limmit, N):
    if i + sum_each_digits(i) == N:
        acceptables.append(i)
k = len(acceptables)
print(k)
for a in acceptables:
    print(a)
