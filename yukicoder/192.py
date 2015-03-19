N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

C = []
m = M
for a in A[::-1]:
    C.append(m//a)
    m -= C[-1]*a
C.reverse()

dp = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    if M%A[i] == 0:
        
