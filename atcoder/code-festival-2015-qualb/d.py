N = int(input())

cells = [0 for i in range(100001)]
for i in range(N):
    s, c = map(int, input().split())
    cnt = 0
    while cnt < c:
        if cells[s] == 0:
            cells[s] = 1
            cnt += 1
        else:
            s += 1
    print(s)
