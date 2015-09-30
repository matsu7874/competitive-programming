N, K = map(int, input().split())
T = [int(input()) for i in range(N)]
for i in range(N - 2):
    if sum(T[i:i + 3]) < K:
        print(i + 3)
        exit()
print(-1)
