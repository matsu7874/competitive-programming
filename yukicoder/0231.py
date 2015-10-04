N = int(input())
max_g = 0
max_i = 0
for i in range(N):
    g, d = map(int, input().split())
    if max_g < g - 30000 * d:
        max_g = g - 30000 * d
        max_i = i + 1
if 3000000 <= max_g * 6:
    print('YES')
    for i in range(6):
        print(max_i)
else:
    print('NO')
