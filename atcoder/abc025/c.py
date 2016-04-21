b = [list(map(int, input().split())) for i in range(2)]
c = [list(map(int, input().split())) for i in range(3)]
sum_score = 0
for lst in [b,c]:
    for row in lst:
        for e in row:
            sum_score += e
def count_score(board):
    key = ''.join(board)
    if key in states:
        return states[key]
    score = 0
    for i in range(2):
        for j in range(3):
            if board[i*3+j] == board[i*3+j+3]:
                score += b[i][j]
            else:
                score -= b[i][j]
    for i in range(3):
        for j in range(2):
            if board[i*3+j] == board[i*3+j+1]:
                score += c[i][j]
            else:
                score -= c[i][j]
    states[key] = score
    return score

def search(turn, board):
    if turn == 9:
        return count_score(board)
    best_score = float('inf') * (-1)**(turn+1)
    best_hand = 0
    for i in range(9):
        if board[i] == '':
            next_board = board[:i] + ['ox'[turn%2]] + board[i+1:]
            n_score = search(turn + 1, next_board)
            if turn % 2 == 0:
                if best_score < n_score:
                    best_hand = i
                    best_score = n_score
            else:
                if best_score > n_score:
                    best_hand = i
                    best_score = n_score
    return best_score

states = {}
best_score = search(0,['','','','','','','','',''])
print((sum_score+best_score)//2, (sum_score-best_score)//2)
