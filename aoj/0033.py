n = int(input())
for i in range(n):
    bs = list(map(int, input().split()))
    lanes = [0,0]
    for j in bs:
        if j > lanes[0] and  j > lanes[1]:
            lanes[lanes.index(max(lanes))] = j
        elif j>lanes[0]:
            lanes[0] = j
        elif j>lanes[1]:
            lanes[1] = j
        else:
            print('NO')
            break
    else:
        print('YES')
