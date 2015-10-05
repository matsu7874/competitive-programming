R, C, K = map(int, input().split())
N = int(input())

candy = []
row_sum = [0] * R
col_sum = [0] * C
for i in range(N):
    r, c = map(int, input().split())
    candy.append((r - 1, c - 1))
    row_sum[r - 1] += 1
    col_sum[c - 1] += 1

col_sum_deg = [0] * 100001
for cs in col_sum:
    col_sum_deg[cs] += 1

cnt = 0
for rs in row_sum:
    if K >= rs:
        cnt += col_sum_deg[K - rs]

for i, j in candy:
    if row_sum[i] + col_sum[j] == K:
        cnt -= 1
    if row_sum[i] + col_sum[j] == K + 1:
        cnt += 1
print(cnt)
