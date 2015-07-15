def main():
    target = 100
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(1,target):
        for j in range(i,target+1):
            dp[j] += dp[j-i]
    print(dp[target])

if __name__ == '__main__':
    main()
