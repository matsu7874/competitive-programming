import itertools
N = int(input())
for s in itertools.product('abc', repeat=N):
    print(''.join(s))
