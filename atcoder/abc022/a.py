N, S, T = map(int, input().split())
W = int(input())
cnt = 0
if S <= W <= T:
    cnt += 1
for i in range(N - 1):
    W += int(input())
    if S <= W <= T:
        cnt += 1
print(cnt)
