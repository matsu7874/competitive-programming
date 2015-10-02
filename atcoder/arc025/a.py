D = list(map(int, input().split()))
J = list(map(int, input().split()))
total = 0
for i in range(7):
    total += max(D[i], J[i])
print(total)
