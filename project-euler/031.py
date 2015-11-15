"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [[0 for j in range(201)] for i in range(len(coins))]
    for i in range(201):
        dp[0][i] = 1
    for i in range(1, len(coins)):
        for j in range(201):
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
    print(dp[len(coins)-1][200])

if __name__ == '__main__':
    main()
