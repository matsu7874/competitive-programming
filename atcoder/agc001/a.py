n = int(input()) * 2
l = list(map(int, input().split()))
l.sort()
total = 0
for i in range(1, n, 2):
    total += l[i - 1]
print(total)
