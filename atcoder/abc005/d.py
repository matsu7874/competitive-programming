def read_data():
    N = int(input())
    D = [[int(x) for x in input().split()] for i in range(N)]
    Q = int(input())
    P = [int(input()) for i in range(Q)]
    return N, D, P

def prepare(N, D):
    delicious = [[0 for j in range(N+1)] for i in range(N+1)]
    for i in range(N):
        for j in range(N):
            delicious[i+1][j+1] = D[i][j] + delicious[i+1][j] + delicious[i][j+1] - delicious[i][j]
    return delicious

def solve(N, delicious, p):
    max_delicious = 0
    w = max(p//N, 1)
    while w<=p and w<=N and 1<=p//w:
        if p%w != 0 or p//w > N:
            w += 1
            continue
        h = p//w
        for i in range(N-w+1):
            for j in range(N-h+1):
                d = delicious[i][j] - delicious[i+w][j] - delicious[i][j+h] + delicious[i+w][j+h]
                max_delicious = max(max_delicious, d)
        w += 1
    return max_delicious

if __name__ == '__main__':
    N, D, P = read_data()
    delicious = prepare(N, D)
    answers = [solve(N, delicious, p) for p in range(1,N**2+1)]
    for p in P:
        print(max(answers[:p]))
