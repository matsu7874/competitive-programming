n, m = map(int, input().split())
a = [0 for i in range(m + 2)]
total_score = 0
for i in range(n):
    l, r, s = map(int, input().split())
    a[l] += s
    a[r + 1] -= s
    total_score += s
min_score = float('inf')
for i in range(1, m + 1):
    a[i] += a[i - 1]
    min_score = min(min_score, a[i])
print(total_score - min_score)
