n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (n+1)
for i in range(n):
    b[i+1] = a[i] + b[i]
total = 0
for i in range(n-k+1):
    total += b[i+k] - b[i]
print(total)
