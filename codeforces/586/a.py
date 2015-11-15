N = int(input())
A = list(map(int, input().split()))
total = 0
for i in range(N):
    if A[i] == 1:
        total += 1
    else:
        if total > 0:
            if (i - 1 >= 0 and A[i - 1] == 1) and (i + 1 < N and A[i + 1] == 1):
                total += 1
print(total)
