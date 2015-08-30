N, M = map(int, input().split())
D = [i for i in range(N + 1)]
listening = 0
for _ in range(M):
    d = int(input())
    D[d], D[listening] = D[listening], D[d]
    listening = d
for i in range(1, N + 1):
    print(D.index(i))
