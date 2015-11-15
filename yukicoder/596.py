def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    max_s = S[-1]
    dp = [[999999999 for j in range(max_s+1)] for i in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1+i
    for i in range(S[0]+1):
        dp[0][i] = i+1
    for i in range(1, N+1):
        for j in range(1, S[i]+1):
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            for k in range(j):
                dp[i][j] = min(dp[i][j], dp[i][j-k-1]+dp[i][k])
    ans = ''
    for i in range(max_s+1):
        ans += str(dp[N][i]) + ' '
    print(ans[:-1])
    # for row in dp:
    #     print(row)
    

if __name__ == '__main__':
    main()
