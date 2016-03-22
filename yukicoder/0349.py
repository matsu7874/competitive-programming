import collections
n = int(input())
d = collections.defaultdict(int)
for i in range(n):
    d[input()] += 1
for k, v in d.items():
    if v * 2 - 1 > n:
        print('NO')
        exit()
print('YES')
