N = int(input())
H = [int(input()) for i in range(N)]
L = [0] * N
R = [0] * N

for i in range(1, N):
    if H[i - 1] < H[i]:
        L[i] = L[i - 1] + 1
    else:
        L[i] = 0
for i in range(N - 2, -1, -1):
    if H[i + 1] < H[i]:
        R[i] = R[i + 1] + 1
    else:
        R[i] = 0

largest = 0
for i in range(N):
    largest = max(largest, L[i] + 1 + R[i])
print(largest)
