N = int(input())
A = list(set(map(int, input().split())))
A.sort()
max_v = 2**16
dp = [False] * (2**16)
dp[0] = True
for i in range(len(A)):
    for j in range(2**15):
        if not dp[j]:
            continue
        dp[j ^ A[i]] = True
cnt = 0
for i in range(2**16):
    if dp[i]:
        cnt += 1
print(cnt)
