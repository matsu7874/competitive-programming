N, K = map(int, input().split())
print((6 * (N - K) * (K - 1) + 3 * (K - 1) + 3 * (N - K) + 1) / N / N / N)
