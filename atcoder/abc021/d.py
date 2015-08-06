n = int(input())
k = int(input())
ans = 0

F = [0 for x in range(200002)]
def functional(n):
    if F[n] != 0:
        return F[n]
    elif n>1:
        F[n] = n*functional(n-1)
        return F[n]
    else:
        return 1

print((functional(n+k-1)//(functional(k)*functional(n-1)))%1000000007) 