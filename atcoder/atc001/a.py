import collections

def read_data():
    H, W = [int(x) for x in input().split()]
    town = [[c for c in input()] for h in range(H)]
    return H, W, town

def find_start(town):
    for h, row in enumerate(town):
        for w, c in enumerate(row):
            if c == 's':
                return h, w

def solve(H, W, town):
    x, y = find_start(town)
    dq = collections.deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if nx<0 or H<=nx or ny<0 or W<=ny:
                continue
            if town[nx][ny] == 'g':
                return True
            if town[nx][ny] == '.':
                town[nx][ny] = 's'
                dq.append((nx, ny))
    return False

if __name__ == '__main__':
    H, W, town = read_data()
    if solve(H, W, town):
        print('Yes')
    else:
        print('No')