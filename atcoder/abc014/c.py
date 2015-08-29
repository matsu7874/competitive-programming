n = int(input())
N = 1000001
C = [0 for i in range(N + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    C[a] += 1
    C[b + 1] -= 1
max_v = 0
v = 0
for i in range(N):
    v += C[i]
    max_v = max(max_v, v)
print(max_v)
