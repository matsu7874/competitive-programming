def lower_bound(lst, n):
    # ソートされたlst内でlst[index]がn以上かつ最小のindexを返す
    # nを挿入する際にソートが維持される最小のindexを返す
    l = 0
    r = len(lst)
    while l < r:
        m = (l + r) // 2
        if lst[m] >= n:
            r = m
        elif lst[m] < n:
            l = m + 1
    return l


N = int(input())
D = [int(input()) for i in range(N)]
D.sort()
mod = 1000000007

dp = [[0 for j in range(4)] for i in range(N)]
total = [[0 for j in range(4)] for i in range(N)]
ret = 0
cursor = N
for i in range(N - 1, -1, -1):
    cursor = lower_bound(D[:cursor], D[i] // 2)
    while D[cursor + 1] * 2 <= D[i]:
        cursor += 1
    dp[i][0] = 1
    dp[i][1] = cursor
for i in range(N):
    for j in range(3):
        total[i][j] = (total[i - 1][j] + dp[i][j]) % mod
    ret += dp[i][3]
print(ret % mod)
