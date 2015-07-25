def main():
    N,P = [int(x) for x in input().split()]
    T = []
    for i in range(N):
        a,b = [int(x) for x in input().split()]
        T.append((a,b))
    T.sort()
    ans = 0
    dp = [[0 for j in range(P+101)] for i in range(N+1)]
    for i in range(0,N)[::-1]:
        for j in range(P+1+T[i][0]):
            if j<T[i][0]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-T[i][0]] + T[i][1])
                if j-T[i][0] <= P:
                    ans = max(ans, dp[i][j])
    print(ans)


if __name__ == '__main__':
    main()
