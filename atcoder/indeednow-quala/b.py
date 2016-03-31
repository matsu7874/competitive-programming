import collections
n = int(input())
target = collections.Counter()
for c in 'indeednow':
    target[c] += 1
for i in range(n):
    query = collections.Counter()
    for c in input():
        query[c] += 1
    if target == query:
        print('YES')
    else:
        print('NO')
