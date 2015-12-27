D = int(input())
C = ['x'] * 15
C.extend([c for c in input()])
C.extend([c for c in input()])
C.extend(['x'] * 15)

max_holiday = D
for i in range(1, 30):
    cnt = 0
    j = 1
    while C[i - j] == 'o':
        cnt += 1
        j += 1
    j = 0
    while C[i + j] == 'x' and j < D:
        cnt += 1
        j += 1
    while C[i + j] == 'o':
        cnt += 1
        j += 1
    max_holiday = max(max_holiday, cnt)

print(max_holiday)
