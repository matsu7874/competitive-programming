def main():
    INF = float('inf')
    N = int(input())
    Total = int(input())
    A = [int(x) for x in input().split()]
    dp = [INF for i in range(Total + 1)]
    dp[A[0]] = 0
    for i in range(1, N):
        dp_next = [INF for i in range(Total + 1)]
        for j in range(Total + 1):
            if dp[j] == INF:
                continue
            if j + A[i] <= Total:
                dp_next[j + A[i]] = min(dp_next[j + A[i]], dp[j] * 2)
            if j * A[i] <= Total:
                dp_next[j * A[i]] = min(dp_next[j * A[i]], dp[j] * 2 + 1)
        dp = dp_next[:]
    for i in range(N - 1):
        if (dp[Total] >> (N - 2 - i)) % 2 == 1:
            print('*', end='')
        else:
            print('+', end='')
    print()

if __name__ == '__main__':
    main()
