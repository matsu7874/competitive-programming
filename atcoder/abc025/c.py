b = [list(map(int, input().split())) for i in range(2)]
c = [list(map(int, input().split())) for i in range(3)]

sum_score = 0
for lst in [b,c]:
    for row in lst:
        for e in row:
            sum_score += e

BOARD_SIZE = 9
def calc_score():
    score = 0
    for i in range(2):
        for j in range(3):
            if board[i*3+j] == board[i*3+j+3]:
                score += b[i][j]
            if board[j*3+i] == board[j*3+i+1]:
                score += c[j][i]
    return score

def dfs(cur):
    res = float('inf') * (-1)**(cur+1)
    key = 0
    t = 1
    for i in range(BOARD_SIZE):
        key += board[i] * t
        t *= 3
    if memo[cur % 2][key] > -1:
        return memo[cur % 2][key]
    if cur == 9:
        res = calc_score()
    elif cur % 2 == 0:
        for i in range(BOARD_SIZE):
            if board[i] == 0:
                board[i] = 1
                res = max(res, dfs(cur+1))
                board[i] = 0
    else:
        for i in range(BOARD_SIZE):
            if board[i] == 0:
                board[i] = 2
                res = min(res, dfs(cur+1))
                board[i] = 0
    memo[cur % 2][key] = res
    return res

memo = [[-1] * (3**9) for i in range(2)]
board = [0 for i in range(BOARD_SIZE)]
score = dfs(0)
print(score, sum_score-score, sep='\n')
