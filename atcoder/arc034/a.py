N = int(input())
max_point = 0
for i in range(N):
    a, b, c, d, e = map(int, input().split())
    max_point = max(max_point, a + b + c + d + e * 11 / 90)
print(max_point)
