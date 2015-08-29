n = int(input())
N = 1000001
C = [0 for i in range(N)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        C[i] += 1
print(max(C))
