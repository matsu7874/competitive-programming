N = int(input())
A = list(map(int, input().split()))
min_total = float('inf')
blocks = sum(A)
row = 0
while (row + 1)**2 <= blocks:
    row += 1
    while 2 * row - 1 > len(A):
        A.append(0)
    total = 0
    for i in range(row):
        total += max(0, A[i] - (i + 1))
    for i in range(row - 1):
        total += max(0, A[2 * row - 2 - i] - (i + 1))
    for i in range(2 * row - 1, len(A)):
        total += A[i]
    min_total = min(min_total, total)

print(min_total)
