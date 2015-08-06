def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p.sort()
    dp = [False for i in range(10000+1)]
    dp[0] = True
    for i in range(n):
        for j in range(10000, 0-1, -1):
            if dp[j] == True:
                dp[j + p[i]] = True
    print(dp.count(True))

if __name__ == '__main__':
    main()
