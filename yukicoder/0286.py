N = int(input())
M = [int(input()) for i in range(N)]
dp = [1 << 20 for i in range(1 << N + 1)]
dp[0] = 0

bit = 0
while bit < (1 << N)-1:
    discount = 0
    for i in range(N):
        if bit & (1 << i):
            discount += M[i]
        discount %= 1000
    for i in range(N):
        if (bit & (1 << i)) == 0:
            dp[bit | (1 << i)] = min(dp[bit | (1 << i)], dp[bit] + max(0, M[i] - discount))
    bit += 1
print(dp[(1 << N) - 1])
