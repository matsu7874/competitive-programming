m, n, N = map(int, input().split())
total = N
unused = 0
used = N
while unused + used >= m:
    unused = used // m * n
    used = used % m
    total += unused
    used += unused
print(total)
