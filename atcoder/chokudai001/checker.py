A = [list(map(int, input().split())) for i in range(30)]
f = open('out.txt', 'r')
turn = 0
py = -1
px = -1
for line in f:
    y, x = map(int, line.split())
    if ((abs(py-y) == 1 and px-x==0) or (abs(px-x) == 1 and py-y==0)) and A[py][px] == A[y][x]:
        pass
    else:
        turn += 1
    A[y][x] -= 1
    py = y
    px = x
if all([sum(A[i])==0 for i in range(30)]):
    print('SUCCESS')
    print(turn)
else:
    print('MISS')
    print(turn)
