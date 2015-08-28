import sys
sys.setrecursionlimit(10000)


def prime_sieve(n):
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(4, n + 1, 2):
        is_prime[i] = False
    for i in range(3, int(n**0.5 + 1), 2):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
P = prime_sieve(N)
lP = len(P)
win = 1
lose = 0
undefined = -1
F = [undefined for i in range(N + 1)]
F[0] = win
F[1] = win


def dfs(n):
    if F[n] == win:
        return win
    elif F[n] == lose:
        return lose
    else:
        flg = lose
        i = 0
        while i < lP and n - P[i] >= 0:
            if dfs(n - P[i]) == lose:
                F[n] = win
                return win
            i += 1
        F[n] = lose
        return lose

print(['Lose', 'Win'][dfs(N)])
