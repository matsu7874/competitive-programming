N, H, M, T = map(int, input().split())
M += T * (N - 1)
H += M // 60
print(H % 24)
print(M % 60)
