C = list(map(int, input().split()))
min_c = min(C)
p = 0
for i in range(7):
    C[i] -= min_c
mi_c = C.index(0)
for i in range(mi_c):
    C[i] -= 1
D = C[min_c:] + C[:min_c]
for i in range(7):
    D[i] -= D[i-1]
    D[i-1] = 0
if D==[0,0,0,0,0,0,0]:
    print('YES')
else:
    print('NO')
