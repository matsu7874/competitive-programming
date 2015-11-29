import collections
A = []
for i in range(4):
    A += list(map(int, input().split()))
# print(A)
dq = collections.deque()
dq.append([[False] * 16, A[:]])
while dq:
    moved, puzzle = dq.popleft()
    # print(puzzle,moved)
    if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
        print('Yes')
        exit()
    zero = puzzle.index(0)
    if zero >= 4:
        t = puzzle[zero - 4]
        if not moved[t]:
            next_puzzle = puzzle[:]
            next_puzzle[zero] = t
            next_puzzle[zero - 4] = 0
            next_moved = moved[:]
            next_moved[t] = True
            dq.append([next_moved, next_puzzle])
    if zero % 4 > 0:
        t = puzzle[zero - 1]
        if not moved[t]:
            next_puzzle = puzzle[:]
            next_puzzle[zero] = t
            next_puzzle[zero - 1] = 0
            next_moved = moved[:]
            next_moved[t] = True
            dq.append([next_moved, next_puzzle])
    if zero < 12:
        t = puzzle[zero + 4]
        if not moved[t]:
            next_puzzle = puzzle[:]
            next_puzzle[zero] = t
            next_puzzle[zero + 4] = 0
            next_moved = moved[:]
            next_moved[t] = True
            dq.append([next_moved, next_puzzle])
    if zero % 4 < 3:
        t = puzzle[zero + 1]
        if not moved[t]:
            next_puzzle = puzzle[:]
            next_puzzle[zero] = t
            next_puzzle[zero + 1] = 0
            next_moved = moved[:]
            next_moved[t] = True
            dq.append([next_moved, next_puzzle])
print('No')
