R, C, D = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(R)]

max_p = 0
for i in range(R):
    for j in range((D + i) % 2, min(C, D - i + 1), 2):
        max_p = max(max_p, A[i][j])
print(max_p)
