import itertools
N, K = map(int, input().split())
T = [[int(j) for j in input().split()] for i in range(N)]
for s in itertools.product(range(K), repeat=N):
    res = 0
    for i in range(N):
        res ^= T[i][s[i]]
    if res == 0:
        print('Found')
        exit()
print('Nothing')
