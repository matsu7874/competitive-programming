def dfs(tiles, w, h, x, y):
    cnt = 1
    tiles[y][x] = '@'
    for dx,dy in ((0,1), (0,-1), (-1,0), (1,0)):
        if 0<=x+dx<w and 0<=y+dy<h and tiles[y+dy][x+dx]=='.':
            cnt += dfs(tiles, w, h, x+dx, y+dy)
    return cnt

def main():
    while True:
        W,H = [int(x) for x in input().split()]
        if W==0 and H==0:
            exit()
        tiles = [[c for c in input()] for h in range(H)]
        for i in range(H):
            if '@' in tiles[i]:
                Y = i
                X = tiles[i].index('@')
        answer = dfs(tiles, W, H, X, Y)
        print(answer)

if __name__ == '__main__':
    main()
