n, X = map(int, input().split())
A = list(map(int, input().split()))
total = 0
for i in range(n):
    if 2**i & X:
        total += A[i]
print(total)
