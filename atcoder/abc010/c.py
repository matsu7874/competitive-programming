def distance(px, py, qx, qy):
    return ((px - qx) * (px - qx) + (py - qy) * (py - qy))**0.5

txa, tya, txb, tyb, T, V = [int(x) for x in input().split()]
n = int(input())
for i in range(n):
    x, y = [int(x) for x in input().split()]
    if distance(txa, tya, x, y) + distance(txb, tyb, x, y) <= T * V:
        print('YES')
        exit()
print('NO')
