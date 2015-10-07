N = int(input())
L = []
for i in range(N):
    a, b = map(int, input().split())
    L.append(a + 4 * b)
max_l = 0
space = L[0]%2
for i in range(N):
    if L[i] > max_l:
        max_l = L[i]
    if L[i] % 2 != space:
        print(-1)
        exit()
total = 0
for i in range(N):
    total += max_l - L[i]
print(total // 2)
