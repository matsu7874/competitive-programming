N, A, B = map(int, input().split())
S = [int(input()) for i in range(N)]
S.sort()
diff = S[N - 1] - S[0]
if B != 0 and diff == 0:
    print(-1)
else:
    P = B / diff
    Q = A - sum(S) / N * P
    print(P, Q)
