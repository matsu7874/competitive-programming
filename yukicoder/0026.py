N = int(input())
M = int(input())
for i in range(M):
    p,q = [int(x) for x in input().split()]
    if p == N:
        N = q
    elif q == N:
        N = p
print(N)
