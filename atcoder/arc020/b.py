n, c = map(int, input().split())
A = [int(input()) for i in range(n)]
min_cost = n * c+1
for i in range(1,11):
    for j in range(1,11):
        if i == j:
            continue
        cost = n * c
        for k in range(n):
            if (k % 2 == 0 and A[k] == i) or (k % 2 == 1 and A[k] == j):
                cost -= c
        min_cost = min(min_cost, cost)
print(min_cost)
