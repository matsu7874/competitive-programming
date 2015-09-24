N, K = map(int, input().split())
for i in range(N):
    K -= int(input())
    if K <= 0:
        print(i + 1)
        break
