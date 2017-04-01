N = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
total = 0
for i in range(N):
    total += a[i*2 + 1]
print(total)