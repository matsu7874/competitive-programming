N = int(input())
C = list(map(int, input().split()))
vote = sum(C)
deposit = 0
for i in range(N):
    if C[i] <= vote / 10:
        deposit += 30
print(deposit)
