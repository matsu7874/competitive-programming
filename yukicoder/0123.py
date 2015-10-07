N, M = map(int, input().split())
A = list(map(int, input().split()))
C = [i + 1 for i in range(N)]
for a in A:
    C = C[a - 1:a] +C[:a - 1] + C[a:]
print(C[0])
