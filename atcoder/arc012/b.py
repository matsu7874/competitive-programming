N, va, vb, L = map(int, input().split())
for i in range(N):
    L = L / va * vb
print(L)
