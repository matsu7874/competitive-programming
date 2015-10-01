N, A, B = map(int, input().split())
print(max(0, N - 5) * A + min(5, N) * B)
